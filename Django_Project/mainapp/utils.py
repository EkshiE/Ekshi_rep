""" This module is needed for auxiliary functions """
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator

from .models import Group


def get_current_group(request):
    """
    Returns currently selected group ju None
    :param request: Object request
    """
    pk = request.COOKIES.get('current_group')

    if pk:
        try:
            group = Group.objects.get(pk=int(pk))
        except Group.DoesNotExist:
            return None
        return group


def paginate(
        obj: object,
        size: int,
        request: object,
        context: dict,
        var_name: str = 'object_list',
) -> dict:
    """ Paginate object provided by views """

    paginator = Paginator(obj, size)
    page = request.GET.get('page', '1')

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context
