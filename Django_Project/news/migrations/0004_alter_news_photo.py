# Generated by Django 3.2.15 on 2023-01-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/blog', verbose_name='Фото'),
        ),
    ]
