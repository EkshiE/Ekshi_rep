from django.db import models


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

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Билет',
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
