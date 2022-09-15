from http import HTTPStatus

from aiohttp.web_response import Response
from aiohttp_apispec import docs
from disc_backend.db.schema import items_table, imports_table, history_table # , relations_table

from sqlalchemy import select, or_

from .base import BaseDeleteView


class DeleteItemView(BaseDeleteView):
    URL_PATH = r'/delete/{id}'

    @docs(summary='Удаляет объект по указанному в адресе идентификатору. \
    Удаление папки влечет удаление всех связанных объектов. Реализован hard delete.')
    async def delete(self):
        await self.check_id_exists()

        async with self.pg.transaction() as conn:
            subquery = (select([items_table.c.id]).where(items_table.c.parentId == self.item_id))
            query = (items_table.delete()
                                .where(or_((items_table.c.id == self.item_id),
                                           (items_table.c.id.in_(subquery)))))
            await conn.execute(query)

            # query = (relations_table.delete()
            #          .where(or_((relations_table.c.id == self.item_id),
            #                     (relations_table.c.id.in_(subquery)))))
            # await conn.execute(query)

            return Response(status=HTTPStatus.OK)
