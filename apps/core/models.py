import uuid

from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and 'modified'(timestamp) fields.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDPrimaryKeyMixin(models.Model):
    """
    Reusable mixin that provides a UUID field as the primary key.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    """
    Reusable mixin that provides a soft delete functionality.
    """

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class BaseModel(UUIDPrimaryKeyMixin, TimeStampedModel):
    """
    An abstract base class model that combines UUIDPrimaryKeyMixin and TimeStampedModel.(base model inherited by all models in the project)
    """

    class Meta:
        abstract = True
