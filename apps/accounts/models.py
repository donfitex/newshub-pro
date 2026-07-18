import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.core.models import TimeStampedModel

from .managers import UserManager


# Create your models here.
class User(AbstractUser, TimeStampedModel):
    """
    Custom authentication model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, db_index=True)

    objects = UserManager()

    class Meta:
        ordering = ["username"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["username"]),
        ]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Profile(TimeStampedModel):
    """
    User profile information
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True)
    phone_number = PhoneNumberField(region="NG", null=True)
    job_title = models.CharField(max_length=150, blank=True)
    website = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    is_email_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ["user__username"]

    def __str__(self):
        return f"{self.user.username}'s Profile"
