from typing import NoReturn
from app.forum import views
from aiohttp.web import Application


# настраиваем пути, которые будут вести к нашей странице
def setup_forum_routes(app: Application) -> NoReturn:
    """

    :param app:
    """
    app.router.add_get('/', views.index)
