from django.db import models
from tinymce.models import HTMLField
from .helpers import *
from .custom_field import *
from .define import *
from django.conf import settings


# Create your models here.
class Category(models.Model):
    title = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class Feed(models.Model):
#     title = models.CharField(unique=True, max_length=200)
#     slug = models.SlugField(unique=True, max_length=200)
#     status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
#     link = models.CharField(max_length=255)
#     ordering = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
