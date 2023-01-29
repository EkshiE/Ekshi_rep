import aiohttp_jinja2


# создаем функцию, которая будет отдавать html-файл
@aiohttp_jinja2.template('index.html')
async def index(request):
    """


    :param request:
    :return:
    """
    return {'title': 'Наше первое приложение на aiohttp'}
