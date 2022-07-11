from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Fields',
            {
                'fields': (
                    'name',
                    'bio',
                    'image',
                    'phone',
                    'location',
                    'date_birth',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
