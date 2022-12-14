# Generated by Django 3.2.15 on 2022-12-06 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('notes', models.TextField(blank=True, verbose_name='Комментарии')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
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
        ),
        migrations.CreateModel(
            name='TimetableСlasses',
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
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.students', verbose_name='Староста'),
        ),
    ]
