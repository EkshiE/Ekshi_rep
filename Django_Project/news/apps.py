from django.apps import AppConfig


class NewsConfig(AppConfig):
    """Регистрация приложения News"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = 'Новости и объявления'
