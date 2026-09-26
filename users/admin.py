from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Что показывать в списке пользователей
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    # Как выглядит форма редактирования пользователя
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Персональная информация", {
            "fields": ("first_name", "last_name", "avatar", "phone", "country")
        }),
        ("Права", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    # Форма создания пользователя через админку
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )