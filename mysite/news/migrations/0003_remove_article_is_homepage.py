# Generated by Django 3.2.3 on 2023-08-07 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_homepage',
        ),
    ]
