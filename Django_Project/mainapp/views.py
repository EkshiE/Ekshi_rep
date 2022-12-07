from django.shortcuts import render

from .models import Group
from .models import Students
# from .utils import get_current_group
from .utils import paginate


def main(request):
    """
    :param request:
    :return:
    """
    return render(request, 'mainapp/index.html')


def news(request):
    """
    :param request:
    :return:
    """
    return render(request, 'mainapp/news.html')


def homework(request):
    """
    :param request:
    :return:
    """
    return render(request, 'mainapp/homework.html')


def groups(request):
    """
    :param request:
    :return:
    """
    return render(request, 'mainapp/groups.html')


def schedule(request):
    """
    :param request:
    :return:
    """
    return render(request, 'mainapp/schedule.html')


def students_list(request):
    """

    :param request:
    :return:
    """
    current_group = get_current_group(request)

    if current_group:
        students = Students.objects.filter(student_group=current_group)
    else:
        students = Students.objects.all()

    order_by = request.GET.get('order_by')

    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)

        if request.GET.get('request') == 1:
            students = students.reverse()

    contex = paginate(students, 3, request, {}, var_name='students')

    return render(request, 'templates/students_list.html', contex)


def group_list(request):
    """

    :param request:
    :return:
    """
    current_group = get_current_group(request)

    if current_group:
        groups1 = Group.objects.filter(title=current_group)
    else:
        groups1 = Group.objects.all()

    order_by = request.GET.get('order_by')

    if order_by == 'title':
        groups1 = groups1.order_by(order_by)

        if request.GET.get('request') == 1:
            groups1 = groups.reverse()

    contex = paginate(groups1, 3, request, {}, var_name='groups')

    return render(request, 'templates/groups_progress.html', contex)
