"""
Django admin configuration for core app
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _
# The gettext_lazy() function is used to translate the string into the user's language. if the user's language is English, it will return the string as it is. If the user's language is not English, it will return the translated string.

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_staff',
                'is_superuser'
            )
        }),
    )
    # classes=('wide',) is used to make the form wider. This is a default ccs class provided by Django.


admin.site.register(models.User, UserAdmin)
# The UserAdmin class is a configuration class that inherits from BaseUserAdmin.
