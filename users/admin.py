from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from users.models import User


# Register your models here.

class CustomUserAdmin(UserAdmin):
    readonly_fields = (
        "date_joined",
        "last_login",
    )

    fieldsets = (
        (
            "Credentials",
            {
                "fields": ("username", "password"),
            },
        ),
        (
            "Personal Info",
            {
                "fields": ("is_critic", "birthdate"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_superuser",
                    "is_active",
                    "is_staff",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)