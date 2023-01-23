# Generated by Django 3.2.15 on 2023-01-20 07:58

from django.db import migrations, models
import django.db.models.deletion
import mainapp.mixims


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название группы')),
                ('notes', models.TextField(blank=True, verbose_name='Комментарии')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
            bases=(models.Model, mainapp.mixims.SoftDateTimeMixim),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(max_length=256, verbose_name='Дисциплина')),
                ('title', models.CharField(max_length=256, verbose_name='Название темы')),
                ('teacher', models.CharField(max_length=256, verbose_name='Преподаватель')),
                ('homework', models.TextField(blank=True, verbose_name='Домашнее задание')),
                ('abstract', models.TextField(blank=True, verbose_name='Конспект')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('student_group', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Тема занятий',
                'verbose_name_plural': 'Тема занятий',
            },
            bases=(models.Model, mainapp.mixims.SoftDateTimeMixim),
        ),
        migrations.CreateModel(
            name='TimetableClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True, verbose_name='Дата занятий')),
                ('time', models.CharField(max_length=30, null=True, verbose_name='Время занятий')),
                ('discipline', models.CharField(max_length=256, verbose_name='Дисциплина')),
                ('teacher', models.CharField(max_length=256, verbose_name='Преподаватель')),
                ('student_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Расписание занятий',
                'verbose_name_plural': 'Расписание занятий',
            },
            bases=(models.Model, mainapp.mixims.SoftDateTimeMixim),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Отчество')),
                ('birthday', models.DateField(null=True, verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Фото')),
                ('notes', models.TextField(blank=True, verbose_name='Комментарий')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('student_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
            bases=(models.Model, mainapp.mixims.SoftDateTimeMixim),
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.students', verbose_name='Староста'),
        ),
        migrations.CreateModel(
            name='AttendanceJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_journal', models.DateField()),
                ('present_day_1', models.BooleanField(default=False)),
                ('present_day_2', models.BooleanField(default=False)),
                ('present_day_3', models.BooleanField(default=False)),
                ('present_day_4', models.BooleanField(default=False)),
                ('present_day_5', models.BooleanField(default=False)),
                ('present_day_6', models.BooleanField(default=False)),
                ('present_day_7', models.BooleanField(default=False)),
                ('present_day_8', models.BooleanField(default=False)),
                ('present_day_9', models.BooleanField(default=False)),
                ('present_day_10', models.BooleanField(default=False)),
                ('present_day_11', models.BooleanField(default=False)),
                ('present_day_12', models.BooleanField(default=False)),
                ('present_day_13', models.BooleanField(default=False)),
                ('present_day_14', models.BooleanField(default=False)),
                ('present_day_15', models.BooleanField(default=False)),
                ('present_day_16', models.BooleanField(default=False)),
                ('present_day_17', models.BooleanField(default=False)),
                ('present_day_18', models.BooleanField(default=False)),
                ('present_day_19', models.BooleanField(default=False)),
                ('present_day_20', models.BooleanField(default=False)),
                ('present_day_21', models.BooleanField(default=False)),
                ('present_day_22', models.BooleanField(default=False)),
                ('present_day_23', models.BooleanField(default=False)),
                ('present_day_24', models.BooleanField(default=False)),
                ('present_day_25', models.BooleanField(default=False)),
                ('present_day_26', models.BooleanField(default=False)),
                ('present_day_27', models.BooleanField(default=False)),
                ('present_day_28', models.BooleanField(default=False)),
                ('present_day_29', models.BooleanField(default=False)),
                ('present_day_30', models.BooleanField(default=False)),
                ('present_day_31', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.students', unique_for_month='date', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Посещаемость',
            },
            bases=(models.Model, mainapp.mixims.SoftDateTimeMixim),
        ),
    ]
