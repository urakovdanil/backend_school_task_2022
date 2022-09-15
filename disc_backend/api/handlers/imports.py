from http import HTTPStatus
from typing import Generator
from sqlalchemy.sql import func, text

from aiohttp.web_response import Response
from aiohttp_apispec import docs, request_schema

from disc_backend.api.schema import ImportSchema
from disc_backend.db.schema import items_table, imports_table, history_table # , relations_table,
from disc_backend.utils.pg import MAX_QUERY_ARGS

from sqlalchemy.dialects.postgresql import insert

from .base import BaseView


class ImportsView(BaseView):
    URL_PATH = '/imports'

    MAX_CITIZENS_PER_INSERT = MAX_QUERY_ARGS // len(items_table.columns)
    # MAX_RELATIONS_PER_INSERT = MAX_QUERY_ARGS // len(relations_table.columns)

    @classmethod
    def make_elements_table_rows(cls, items, import_id, updateDate) -> Generator:
        possible_keys = ['id', 'url', 'parentId', 'size', 'type']
        for item in items:
            res = {}
            for key in possible_keys:
                try:
                    res[key] = item[key]
                except KeyError:
                    pass
            res['import_id'] = import_id
            res['updateDate'] = updateDate.replace(tzinfo=None)
            yield res

    # @classmethod
    # def make_relations_table_rows(cls, items, import_id) -> Generator:
    #     for item in items:
    #         if item['parentId'] is not None:
    #             yield {
    #                 'import_id': import_id,
    #                 'id': item['id'],
    #                 'parentId': item['parentId'],
    #             }

    @docs(summary='Добавление данных об объектах файловой системы.')
    @request_schema(ImportSchema())
    async def post(self):

        async with self.pg.transaction() as conn:

            items = self.request['data']['items']
            updateDate = self.request['data']['updateDate']

            existing_parents_query = text("""SELECT DISTINCT id FROM items WHERE "type" = 'FOLDER'""")
            existing_parents = []
            for row in await conn.fetch(existing_parents_query):
                existing_parents.append(row['id'])
            for item in items:
                if item['type'] == 'FOLDER':
                    existing_parents.append(item['id'])

            parents_to_update = []
            for item in items:
                if item['type'] == 'FILE' and item['parentId'] not in existing_parents:
                    return Response(
                        body={
                            'data': {
                                'error': f'parent of {item["id"]} does not exist or the mentioned parent is a file'}},
                        status=HTTPStatus.BAD_REQUEST
                    )
                parents_to_update.append(item['parentId'])

            query = imports_table.insert().returning(imports_table.c.import_id)
            import_id = await conn.fetchval(query)

            item_rows_main = self.make_elements_table_rows(items, import_id, updateDate)
            item_rows_history = self.make_elements_table_rows(items, import_id, updateDate)
            # relation_rows = self.make_relations_table_rows(items, import_id)

            query = history_table.insert()
            for chunk in item_rows_history:
                await conn.execute(query.values(chunk))

            query = insert(items_table)
            for chunk in item_rows_main:
                query = (query.values(chunk)
                              .on_conflict_do_update(index_elements=['id'],
                                                     set_={'import_id': query.excluded.import_id,
                                                           'url': query.excluded.url,
                                                           'parentId': query.excluded.parentId,
                                                           'size': query.excluded.size,
                                                           'type': query.excluded.type,
                                                           'updateDate': query.excluded.updateDate}))
                await conn.execute(query)

            # query = insert(relations_table)
            # for chunk in relation_rows:
            #     query = (query.values(chunk)
            #                   .on_conflict_do_update(index_elements=['id'],
            #                                          set_={'import_id': query.excluded.import_id,
            #                                                'parentId': query.excluded.parentId}))
            #     await conn.execute(query)

            all_parents_to_update = set(parents_to_update)
            for parent in parents_to_update:
                str_get_upper_parent = f"""SELECT "parentId" FROM items WHERE id = '{parent}'"""
                get_upper_parent = text(str_get_upper_parent)
                upper_parent = await conn.fetchval(get_upper_parent)
                all_parents_to_update.add(upper_parent)
                while type(upper_parent) == str:
                    str_get_upper_parent = f"""SELECT "parentId" FROM items WHERE id = '{upper_parent}'"""
                    get_upper_parent = text(str_get_upper_parent)
                    upper_parent = await conn.fetchval(get_upper_parent)
                    all_parents_to_update.add(upper_parent)

            query = (items_table.update()
                                .where(items_table.c.id.in_(list(all_parents_to_update)))
                                .values({'updateDate': updateDate.replace(tzinfo=None)}))
            await conn.execute(query)

        return Response(body={'data': {'import_id': import_id}},
                        status=HTTPStatus.OK)
