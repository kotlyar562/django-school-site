from django.contrib import admin

from . models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'author', 'date_add')
    list_filter = ('author', 'date_add')
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
