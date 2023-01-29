import jinja2
import aiohttp_jinja2

from aiohttp import web

from typing import NoReturn
from app.settings import CONFIG, BASE_DIR
from app.store.db.accessor import MySQLAccessor


def setup_config(app: web.Application) -> NoReturn:
    """

    :param app:
    """
    app['config'] = CONFIG


def setup_routes(app: web.Application) -> NoReturn:
    """
    В этой функции производится настройка url-путей для всего приложения

    :param app: Application object
    """
    from app.forum.routes import setup_forum_routes
    setup_forum_routes(app)


def setup_jinja2(app: web.Application) -> NoReturn:
    """
    Настраивает шаблонизатор на использование шаблона в директории
    :param app: Application object
    """
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader(
                             f'{BASE_DIR}/templates')
                         )


def setup_accessors(app: web.Application) -> NoReturn:
    """

    :param app:
    """
    app['db'] = MySQLAccessor()
    app['db'].setup(app)


def setup_app(app: web.Application) -> NoReturn:
    """
    Функция настройки всего приложения
    :param app: Application object
    """
    setup_config(app)
    setup_accessors(app)
    setup_jinja2(app)
    setup_routes(app)


app = web.Application()

if __name__ == "__main__":
    setup_app(app)  # Настраиваем приложение
    web.run_app(app,
                port=CONFIG['port'],
                host=CONFIG['host'],
                )  # Производим запуск сервера
