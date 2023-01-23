from django.db import models
from django.urls import reverse


class News(models.Model):
    """ Новости """

    class Meta:
        verbose_name = u'Новости'
        verbose_name_plural = u'Новости'
        ordering = ['id']

    title = models.CharField(
        max_length=100,
        blank=False,
        verbose_name=u'Название'
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='img/blog/',
        verbose_name=u'Фото',
    )

    summary = models.CharField(
        max_length=255,
        verbose_name=u'Краткое содержание',
    )

    post = models.TextField(
        blank=True,
        verbose_name=u'Текст новости',
    )

    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Время создания',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Возвращает объект по id
        """
        return reverse('post', kwargs={'post_id': self.pk})
