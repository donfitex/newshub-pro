from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


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
    list_filter = ("is_staff", "is_active", "is_email_verified")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                    "bio",
                    "phone_number",
                    "job_title",
                    "website",
                    "facebook_url",
                    "x_url",
                    "linkedin_url",
                    "instagram_url",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("username", "email", "phonenumber")
    ordering = ("username",)
