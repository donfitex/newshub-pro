from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the user model.
    """

    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields,
        )
