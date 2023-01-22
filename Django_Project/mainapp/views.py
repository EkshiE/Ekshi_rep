
from django.shortcuts import render

from .models import AttendanceJournal


def main(request):
    """
    :param request:
    :return:
    """
    return render(request, 'templates/index.html')


def homework(request):
    """
    :param request:
    :return:
    """
    return render(request, 'templates/mainapp/homework.html')


def group(request):
    """
    :param request:
    :return:
    """
    posts = AttendanceJournal.objects.all()
    return render(request, 'templates/mainapp/group.html', {'posts': posts})


def timetable(request):
    """
    :param request:
    :return:
    """
    return render(request, 'templates/mainapp/timetable.html')

# def attendance(request):
#     """
#     :param request:
#     :return:
#     """
#     return render(request, 'attendance.html')
#
#
# def students_list(request):
#     """
#
#     :param request:
#     :return:
#     """
#     current_group = get_current_group(request)
#
#     if current_group:
#         students = Students.objects.filter(student_group=current_group)
#     else:
#         students = Students.objects.all()
#
#     order_by = request.GET.get('order_by')
#
#     if order_by in ('last_name', 'first_name', 'ticket'):
#         students = students.order_by(order_by)
#
#         if request.GET.get('request') == 1:
#             students = students.reverse()
#
#     contex = paginate(students, 3, request, {}, var_name='students')
#
#     return render(request, 'group_list.html', contex)
#
#
# def group_list(request):
#     """
#
#     :param request:
#     :return:
#     """
#     current_group = get_current_group(request)
#
#     if current_group:
#         groups1 = Group.objects.filter(title=current_group)
#     else:
#         groups1 = Group.objects.all()
#
#     order_by = request.GET.get('order_by')
#
#     if order_by == 'title':
#         groups1 = groups1.order_by(order_by)
#
#         if request.GET.get('request') == 1:
#             groups1 = group.reverse
#
#     contex = paginate(groups1, 3, request, {}, var_name='groups')
#
#     return render(request, 'mainapp/group.html', contex)
#
#
# class AttendanceView(AttendanceJournal):
#     """ Посещаемость"""
#     template_name = 'mainapp/group.html'
#
#     def get_context_data(self, **kwargs):
#         """ Get- метод для получения контекста из TemplateView класса """
#
#         global next_month, prev_month
#         contex = super().get_context_data(**kwargs)
#         # проверка- если нам нужно вывести какие-то месяца
#         if self.request.GET.get('month'):
#             month = datetime.strptime(
#                 self.request.GET['month'],
#                 '%Y-%m-%d',
#             ).date()
#
#         else:
#             today = datetime.today()
#             month = date(today.year, today.month, 1)
#             # определяем следующий месяц
#             next_month = month + relativedelta(month=1)
#             prev_month = month - relativedelta(month=1)
#
#         contex['next_month'] = next_month.strftime('%Y-%m-%d')
#         contex['prev_month'] = prev_month.strftime('%Y-%m-%d')
#         contex['year'] = month.year
#         contex['month_verbose'] = month.strftime('%B')
#         contex['car_month'] = month.strftime('%Y-%m-%d')
#
#         m_years, m_month = month.year, month.month
#         number_of_days = monthrange(m_years, m_month)[1]
#         contex['month_header'] = [
#             {'day': day,
#              'verbose': day_abbr[weekday(m_years, m_month, day)][:2]
#              } for day in range(1, number_of_days + 1)
#         ]
#         if kwargs.get('pk'):
#             queryset = [Students.objects.get(pk=kwargs.get('pk'))]
#         else:
#             queryset = Students.objects.all().order_by('last_name')
#
#         update_url = reverse('attendance')
#         students = []
#         days = []
#         for student in queryset:
#             try:
#                 attendance = AttendanceJournal.objects.get(
#                     student=student,
#                     date_journal=month,
#                 )
#             except AttendanceJournal.DoesNotExist:
#                 attendance = None
#
#             for day in range(1, number_of_days + 1):
#                 days.append({
#                     'day': day,
#                     'present': attendance and getattr(
#                         attendance, f'present_day_{day}', False,
#                     ) or False,
#                     'date': date(m_years, m_month, day).strftime('%Y-%m-%d')
#                 })
#
#             students.append({
#                 'fullname': f'{student.last_name}'
#                             f'{student.first_name}'
#                             f'{student.middle_name}',
#                 'days': days,
#                 'id': student.id,
#                 'update_url': update_url,
#             })
#         contex['students'] = students
#         return contex
#
#     @staticmethod
#     def post(request, *args, **kwargs):
#         """Для внесения правок """
#         data = request.POST
#
#         current_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
#         month = date(current_date.year, current_date.month, 1)
#         present = data['present'] and True or False
#         student = Students.objects.get(pk=data['pk'])
#
#         journal = AttendanceJournal.objects.get_or_create(
#             student=student, date_journal=month
#         )[0]
#         setattr(journal, f'present_day_{current_date.day}', present)
#         journal.save()
#
#         return JsonResponse({'status': 'success'})
