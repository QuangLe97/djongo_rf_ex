from django.contrib import admin

# Register your models here.
from djongo_app.models import Tag, ArticleEntry, Author


@admin.register(ArticleEntry)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
