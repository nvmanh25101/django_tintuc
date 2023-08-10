# Generated by Django 3.2.3 on 2023-08-07 08:47

from django.db import migrations, models
import django.db.models.deletion
import news.helpers
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('is_homepage', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('ordering', models.IntegerField(default=0)),
                ('special', models.BooleanField(default=False)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(null=True, upload_to=news.helpers.get_file_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
            ],
        ),
    ]