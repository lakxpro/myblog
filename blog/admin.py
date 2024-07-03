from django.contrib import admin
from .models import Tag, Article, ArticleTag


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    exclude = ("image_thumb",)
    search_fields = ("title", "content")
    inlines = [ArticleTagInline]
