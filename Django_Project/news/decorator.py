from functools import wraps
from django.db.models import F
from django.db import transaction

from mainapp.models import News


def counted(f):
    """
    Счетчик просмотров
    """

    @wraps(f)
    def decorator(request, *args, **kwargs):
        """
        Счетчик просмотров
        """
        with transaction.atomic():
            counter, created = News.objects.get_or_create(url=request.path)
            counter.count = F('count') + 1
            counter.save()
        return f(request, *args, **kwargs)

    return decorator
