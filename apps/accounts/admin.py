from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the User model.
    """

    model = User
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )

    list_filter = ("is_staff", "is_active")

    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
        "job_title",
        "is_email_verified",
    )

    search_fields = (
        "user__username",
        "phone_number",
    )
