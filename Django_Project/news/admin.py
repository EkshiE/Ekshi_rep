from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


class NewsAdmin(admin.ModelAdmin):
    """ Форматирование новостей в Admin"""

    list_display = (
        'title',
        'summary',
        'photo',
        'time_create'
    )
    list_display_links = ('title', 'time_create')
    search_fields = ('title', 'time_create')

    @staticmethod
    def photo(obj):
        """Вставка фото
        :param obj: файл
        """
        return mark_safe(f'<imj src="{obj.blog.url}"')


admin.site.register(News, NewsAdmin)
