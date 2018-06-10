from django.contrib import admin
from . models import Group, Svedenie


class SvedeniaAdmin(admin.ModelAdmin):
    list_display = ('title', 'group_title', 'number')
    search_fields = ('title',)
    list_filter = ['group__title']
    list_editable = ('number',)

    def group_title(self, obj):
        return obj.group.title

    group_title.short_description = 'Раздел'
    group_title.admin_order_field = 'group__title'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')
    list_editable = ('number',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Svedenie, SvedeniaAdmin)
admin.site.register(Group, GroupAdmin)
