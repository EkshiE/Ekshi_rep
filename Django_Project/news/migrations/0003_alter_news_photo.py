# Generated by Django 3.2.15 on 2023-01-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20230120_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/blog', verbose_name='Фото'),
        ),
    ]