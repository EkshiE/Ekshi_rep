# Generated by Django 3.2.15 on 2023-01-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='img/blog', verbose_name='Фото')),
                ('summary', models.CharField(max_length=255, verbose_name='Краткое содержание')),
                ('post', models.TextField(blank=True, verbose_name='Текст новости')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новости',
            },
        ),
    ]
