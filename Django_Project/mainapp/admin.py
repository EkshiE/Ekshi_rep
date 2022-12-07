from django.contrib import admin

from .forms import StudentFormAdmin
from .models import BlogPost
from .models import Group
from .models import Students
from .models import TimetableClasses
from .models import Topic


class StudentsAdmin(admin.ModelAdmin):
    """ Форматирование студентов в Admin"""

    list_display = [
        'last_name',
        'first_name',
        'middle_name',
        'student_group',
        'photo',
    ]
    list_display_links = ['last_name']
    list_editable = ['student_group']
    list_filter = ['student_group']
    search_fields = [
        'last_name',
        'first_name',
        'middle_name',
        'student_group',
    ]
    list_per_page = 5
    ordering = ['last_name']
    form = StudentFormAdmin

    @staticmethod
    def photo(obj):
        """Вставка фото
        :param obj: фаил
        """
        return make_safe(
            f'<imj src="{obj.photo.url}"'
            f' height="30", wight="30">'
        )

    # @staticmethod
    # def view_on_site(obj):
    #     """Перебрасывает на форму регистрации.
    #     :param obj
    #     """
    #     return reverse(
    #         viewname='student_edit',
    #         kwargs={'pk': obj.pk},
    #     )


class GroupAdmin(admin.ModelAdmin):
    """ Форматирование студентов в Admin"""

    list_display = [
        'title',
        'leader',
    ]
    list_display_links = ['title', 'leader']
    list_filter = ['title']
    search_fields = ['title', 'leader']
    list_per_page = 5
    ordering = ['leader']


class TimetableClassesAdmin(admin.ModelAdmin):
    """ Форматирование Расписания в Admin"""

    list_display = [
        'data',
        'time',
        'discipline',
        'teacher',
        'student_group'

    ]

    list_filter = ['data', 'student_group', 'teacher']
    search_fields = ['teacher', 'discipline']
    list_per_page = 10


admin.site.register(Students, StudentsAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Topic)
admin.site.register(TimetableClasses, TimetableClassesAdmin)
admin.site.register(BlogPost)