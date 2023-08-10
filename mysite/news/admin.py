from django.contrib import admin

# Register your models here.
from .models import Category, Article, Comment
from .define import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_homepage", "layout", "status", "ordering")
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ("is_homepage", "layout", "status")
    search_fields = ("title", "slug")

    class Media:
        css = ADMIN_SRC_CSS
        js = ADMIN_SRC_JS


admin.site.register(Category, CategoryAdmin)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "ordering")
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ("status", "special", "publish_date", "category")
    search_fields = ("title", "slug")
    inlines = [CommentInline]

    class Media:
        css = ADMIN_SRC_CSS
        js = ADMIN_SRC_JS


admin.site.register(Article, ArticleAdmin)

# class FeedAdmin(admin.ModelAdmin):
#     list_display = ("title", "slug", "status", "ordering")
#     # prepopulated_fields = {'slug': ('title',)}
#     list_filter = ("status",)
#     search_fields = ("title", "slug")
#
#     class Media:
#         js = ADMIN_SRC_JS
#
#
# admin.site.register(Feed, FeedAdmin)

admin.site.site_header = ADMIN_SITE_HEADER
