from aiohttp.web_exceptions import HTTPNotFound
from aiohttp.web_urldispatcher import View
from asyncpgsa import PG
from sqlalchemy import exists, select

from disc_backend.db.schema import imports_table, items_table

from .query import UPDATE_SIZE_QUERY


class BaseView(View):
    URL_PATH: str

    def check_parent_id(self):
        pass

    @property
    def pg(self) -> PG:
        return self.request.app['pg']

    async def update_sizes(self, items):
        if 'children' not in items.keys():
            if items['size'] is None:
                return 0
            return items['size']
        else:
            children_sizes = [await self.update_sizes(child) for child in items['children']]
            if len(children_sizes) == 0:
                items['size'] = 0
            else:
                items['size'] = sum([size for size in children_sizes if size is not None])
            await self.pg.fetchrow(UPDATE_SIZE_QUERY.bindparams(id=items['id'], size=items['size']))
            return items['size']


class BaseUpdatesView(BaseView):

    @property
    def request_date(self):
        try:
            return str(self.request.rel_url.query['date'])[:19]
        except KeyError:
            return None


class BaseNodeView(BaseView):

    @property
    def item_id(self):
        return str(self.request.match_info.get('id'))

    async def check_id_exists(self):
        query = select([
            exists().where(items_table.c.id == self.item_id)
        ])
        if not await self.pg.fetchval(query):
            raise HTTPNotFound()


class BaseDeleteView(BaseView):
    @property
    def item_id(self):
        return str(self.request.match_info.get('id'))

    async def check_id_exists(self):
        query = select([
            exists().where(items_table.c.id == self.item_id)
        ])
        if not await self.pg.fetchval(query):
            raise HTTPNotFound()


class BaseImportView(BaseView):
    @property
    def import_id(self):
        return int(self.request.match_info.get('import_id'))

    async def check_import_exists(self):
        query = select([
            exists().where(imports_table.c.import_id == self.import_id)
        ])
        if not await self.pg.fetchval(query):
            raise HTTPNotFound()
