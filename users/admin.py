from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        'id',
        'email',
        'username',
        'type',
        'is_staff',
        'is_superuser',
    )

    list_filter = (
        'type',
        'is_staff',
        'is_superuser',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'Дополнительные поля',
            {
                'fields': (
                    'type',
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Дополнительные поля',
            {
                'fields': (
                    'email',
                    'type',
                )
            },
        ),
    )