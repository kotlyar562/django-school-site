from django.contrib import admin

from . models import News


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('title', 'date_add')
    list_filter = ('date_add', 'important')
    ordering = ('-date_add',)


admin.site.register(News, NewsAdmin)
