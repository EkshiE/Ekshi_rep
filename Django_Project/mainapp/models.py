from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixims import SoftDateTimeMixim


class Students(models.Model, SoftDateTimeMixim):
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

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Group(models.Model, SoftDateTimeMixim):
    """ Group model """

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Название группы',
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

    def __str__(self):
        if self.leader:
            return (f'{self.title}'
                    )
        return f' {self.title}'


class Topic(models.Model, SoftDateTimeMixim):
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
        _('Название темы'),
        null=False,
        max_length=256,
        blank=False,
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

    def __str__(self):
        return (f'Дисциплина {self.discipline}, тема: {self.title}'
                f' преподаватель:{self.teacher}'
                )


class TimetableClasses(models.Model, SoftDateTimeMixim):
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

    def __str__(self):
        return (f'Дата и время {self.time},{self.discipline}-'
                f' преподаватель:{self.teacher}'
                )


class AttendanceJournal(models.Model, SoftDateTimeMixim):
    """ Модель Журнал посещаемости"""

    class Meta(SoftDateTimeMixim):
        verbose_name = u'Посещаемость'

    student = models.ForeignKey(
        'Students',
        verbose_name='Студент',
        blank=False,
        unique_for_month='date',
        on_delete=models.PROTECT,
    )

    date_journal = models.DateField(
        blank=False,

    )

    present_day_1 = models.BooleanField(default=False)
    present_day_2 = models.BooleanField(default=False)
    present_day_3 = models.BooleanField(default=False)
    present_day_4 = models.BooleanField(default=False)
    present_day_5 = models.BooleanField(default=False)
    present_day_6 = models.BooleanField(default=False)
    present_day_7 = models.BooleanField(default=False)
    present_day_8 = models.BooleanField(default=False)
    present_day_9 = models.BooleanField(default=False)
    present_day_10 = models.BooleanField(default=False)
    present_day_11 = models.BooleanField(default=False)
    present_day_12 = models.BooleanField(default=False)
    present_day_13 = models.BooleanField(default=False)
    present_day_14 = models.BooleanField(default=False)
    present_day_15 = models.BooleanField(default=False)
    present_day_16 = models.BooleanField(default=False)
    present_day_17 = models.BooleanField(default=False)
    present_day_18 = models.BooleanField(default=False)
    present_day_19 = models.BooleanField(default=False)
    present_day_20 = models.BooleanField(default=False)
    present_day_21 = models.BooleanField(default=False)
    present_day_22 = models.BooleanField(default=False)
    present_day_23 = models.BooleanField(default=False)
    present_day_24 = models.BooleanField(default=False)
    present_day_25 = models.BooleanField(default=False)
    present_day_26 = models.BooleanField(default=False)
    present_day_27 = models.BooleanField(default=False)
    present_day_28 = models.BooleanField(default=False)
    present_day_29 = models.BooleanField(default=False)
    present_day_30 = models.BooleanField(default=False)
    present_day_31 = models.BooleanField(default=False)

    def __repr__(self):
        return (
            f'{self.student.last_name} '
            f'{self.date_journal.month}'
            f'{self.date_journal.year}'
        )
