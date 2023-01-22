from django.utils.safestring import mark_safe
from django.contrib import admin

from .forms import StudentFormAdmin
from django.urls import reverse

from .models import Group
from .models import Students


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
        :param obj: файл
        """
        return mark_safe(
            f'<imj src="{obj.photo.url}"'
            f' height="30", wight="30">'
        )

    # @staticmethod
    # def view_on_site(obj):
    #     """Перебрасывает на форму регистрации.
    #     :param obj
    #     """
    #     return reverse(
    #         rename='student_edit',
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


admin.site.register(Students, StudentsAdmin)
admin.site.register(Group, GroupAdmin)
