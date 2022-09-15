import json

from aiohttp.web_response import Response
from aiohttp_apispec import docs

from disc_backend.db.schema import items_table

from disc_backend.utils.pg import SelectQuery

from .base import BaseNodeView
from .query import ITEMS_QUERY, HIERARCHY_QUERY


class NodesView(BaseNodeView):
    URL_PATH = r'/nodes/{id}'

    def get_nested(self, flat_data):
        res = {}
        for i in range(len(flat_data)):
            if flat_data[i]['type'] == 'FOLDER':
                flat_data[i]['children'] = []
            res[flat_data[i]['id']] = flat_data[i]
            try:
                if flat_data[i]['parentId']:
                    parent = res[flat_data[i]['parentId']]
                    if parent:
                        if 'children' not in parent.keys():
                            parent['children'] = []
                        parent['children'].append(flat_data[i])
            except KeyError:
                pass

        res = json.dumps(res[self.item_id], default=lambda x: x.strftime('%Y-%m-%dT%H:%M:%S') + 'Z')
        return res

    @docs(summary='Выгрузка данных об объекте, идентификатор которого был передан в адресе')
    async def get(self):
        await self.check_id_exists()

        async with self.pg.transaction() as conn:
            h_query = HIERARCHY_QUERY
            h_query = h_query.bindparams(id=self.item_id)

            dicted_res = []
            for item in await conn.fetch(h_query):
                dicted_res.append(dict(item))

            if len(dicted_res) > 0:
                nested_res = self.get_nested(dicted_res)
                await self.update_sizes(json.loads(nested_res))
                dicted_res = []
                for item in await conn.fetch(h_query):
                    dicted_item = dict(item)
                    if dicted_item['type'] == 'FILE':
                        dicted_item['children'] = None
                    dicted_res.append(dicted_item)
                nested_res = self.get_nested(dicted_res)
                return Response(body=nested_res)

            query = ITEMS_QUERY.where(items_table.c.id == self.item_id)
            body = SelectQuery(query=query, transaction_ctx=self.pg.transaction())
            return Response(body=body)
