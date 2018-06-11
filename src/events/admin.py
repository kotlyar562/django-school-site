from django.contrib import admin

from . models import Event


class EventAdmin(admin.ModelAdmin):
    list_filter = ('date_begin', 'etype')
    ordering = ('date_begin',)
    list_display = ('title', 'etype', 'date_begin', 'date_end', )


admin.site.register(Event, EventAdmin)
