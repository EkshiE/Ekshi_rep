# Generated by Django 3.2.15 on 2023-01-21 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_news_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['id'], 'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
    ]
