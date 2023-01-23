from .utils import get_current_group


def group_processor(request):
    """ Процессор """
    return {'GROUPS': get_current_group(request)}
