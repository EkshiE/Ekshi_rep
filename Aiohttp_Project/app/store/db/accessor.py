from aiohttp import web
from app.store.db.models import Message
from app.store.db.models import DB
from typing import NoReturn


class MySQLAccessor:
    """ """

    def __int__(self):
        self.massage = Message
        self.db = None

    def setup(self, app: web.Application) -> NoReturn:
        """  """

        app.on_startup(self._connection)
        app.on_cleanup(self._disconnection)

    async def _connection(self, app: web.Application):
        self.config = app['config']['databases']
        await DB.set_bint(self.config['databases_url'])
        self.db = DB

    async def _disconnection(self):
        if self.db:
            await self.db.pop_bind().close()
