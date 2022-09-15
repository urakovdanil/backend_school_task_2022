from sqlalchemy.sql import text

from aiohttp.web_response import Response

from .base import BaseUpdatesView
from disc_backend.utils.pg import SelectQuery


class UpdatesView(BaseUpdatesView):
    URL_PATH = '/updates'

    async def get(self):
        if self.request_date is None:
            query = text("""SELECT id, url, "parentId", "updateDate" 
                            FROM items 
                            WHERE "updateDate" > current_timestamp - INTERVAL '1 DAY'""")
        else:
            str_query = f"""SELECT id, url, "parentId", "updateDate" 
                            FROM items 
                            WHERE "updateDate" BETWEEN CAST('{self.request_date}' AS timestamp) - INTERVAL '1 DAY' AND 
                                                       CAST('{self.request_date}' AS timestamp)"""
            query = text(str_query)
        body = SelectQuery(query, self.pg.transaction())
        return Response(body=body)
