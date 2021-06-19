from django.contrib import admin

# Register your models here.
from djongo_app.forms import ArticleEntryChangeListForm
from djongo_app.models import Tag, ArticleEntry, Author


#
# class AuthorInline(admin.TabularInline):
#     model = ArticleEntry.authors.through
#     fields = ['auth_name']
#     readonly_fields = ['auth_name']
#
#     def auth_name(self, instance):
#         print(instance.authors.name)
#         print(instance.author.name)
#         return instance.authorS.name
#     auth_name.short_description = 'authors',

#
# class AuthorAdminInline(admin.TabularInline):
#     model = ArticleEntry.authors.through
#
# class AuthorAdmin(admin.TabularInline):
#     inlines = (AuthorAdminInline,)
#     exclude = ('authors',)

@admin.register(ArticleEntry)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleEntryChangeListForm
    fieldsets = (
        (None, {
            'fields': ('content', 'blog', 'authors',),
        }),
    )
    pass
    # filter_horizontal = ('articles',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
