from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Students(models.Model):
    """ Student model """

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенты'

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Фамилия',
    )

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Имя',
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u'Отчество',
        default='',
    )

    birthday = models.DateField(
        blank=False,
        null=True,
        verbose_name=u'Дата рождения',
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='photo',
        verbose_name=u'Фото',
    )

    student_group = models.ForeignKey(
        'Group',
        blank=False,
        null=True,
        verbose_name=u'Группа',
        on_delete=models.PROTECT,
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u'Комментарий',
    )

    create_at = models.DateTimeField(
        blank=False,
        null=True,
        editable=True,
        auto_now_add=True,
        verbose_name=u'Время создания',

    )

    def __repr__(self):
        return f'<Студент {self.last_name} {self.first_name}>'


class Group(models.Model):
    """ Group model """

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Название',
    )

    leader = models.OneToOneField(
        'Students',
        blank=True,
        null=True,
        verbose_name=u'Староста',
        on_delete=models.SET_NULL,
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u'Комментарии',
    )

    create_at = models.DateTimeField(
        blank=False,
        null=True,
        editable=True,
        auto_now_add=True,
        verbose_name=u'Время создания',

    )

    def __repr__(self):
        if self.leader:
            return (f'<Группа {self.title}, староста- {self.leader.first_name}'
                    f' {self.leader.last_name}>'
                    )
        return f'<Группа {self.title}>'


class Topic(models.Model):
    """ Topic model """

    class Meta:
        verbose_name = u'Тема занятий'
        verbose_name_plural = u'Тема занятий'

    discipline = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Дисциплина',
    )
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Название темы',
    )

    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Преподаватель',
    )

    student_group = models.OneToOneField(
        'Group',
        blank=False,
        null=True,
        verbose_name=u'Группа',
        on_delete=models.PROTECT,
    )

    homework = models.TextField(
        blank=True,
        verbose_name=u'Домашнее задание',
    )
    abstract = models.TextField(
        blank=True,
        verbose_name=u'Конспект',
    )

    create_at = models.DateTimeField(
        blank=False,
        null=True,
        editable=True,
        auto_now_add=True,
        verbose_name=u'Время создания',

    )

    def __repr__(self):
        return (f'<Дисциплина {self.discipline}, тема: {self.title}'
                f' преподаватель:{self.teacher}>'
                )


class TimetableClasses(models.Model):
    """Model: Timetable of classes  """

    class Meta:
        verbose_name = u'Расписание занятий'
        verbose_name_plural = u'Расписание занятий'

    data = models.DateField(
        blank=False,
        null=True,
        verbose_name=u'Дата занятий',
    )
    time = models.CharField(
        max_length=30,
        blank=False,
        null=True,
        verbose_name=u'Время занятий',
    )

    discipline = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Дисциплина',
    )

    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Преподаватель',
    )
    student_group = models.ForeignKey(
        'Group',
        blank=False,
        null=True,
        verbose_name=u'Группа',
        on_delete=models.PROTECT,
    )

    def __repr__(self):
        return (f'<Дата {self.time}, дисциплина: {self.discipline}'
                f' преподаватель:{self.teacher}>'
                )


class BlogPost(models.Model):
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    body = RichTextUploadingField()

    def __str__(self):
        return self.title
