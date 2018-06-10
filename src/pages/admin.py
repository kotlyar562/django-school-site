from django.contrib import admin

from . models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'group')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('group',)
    search_fields = ('title',)

admin.site.register(Page, PageAdmin)
