from . models import User
from .forms import AdminUserAddForm, AdminUserChangeForm
from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from redactor.widgets import RedactorEditor


class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserAddForm
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Информация', {'fields': (
            'first_name',
            'last_name',
            'email',
            'photo',
            'post',
            'stag',
            'rank',
            'statement',
        )}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_display = ('last_name', 'first_name', 'username', 'email', 'is_staff')
    list_display_links = ('last_name', 'username')

admin.site.register(User, UserAdmin)
