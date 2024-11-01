import uuid

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.fields import UUIDField
from model_utils.models import TimeStampedModel

__all__ = [
    "BaseModel",
    "WithSocialTargetMixin",
]

User = get_user_model()


class BaseModel(
    TimeStampedModel,
):
    id = UUIDField(default=uuid.uuid4)

    class Meta:
        abstract = True


class WithSocialTargetMixin(models.Model):
    target = GenericForeignKey(
        fk_field="target_id",
    )
    target_id = models.UUIDField(
        blank=False,
        null=False,
        editable=False,
        verbose_name=_("Target ID"),
    )
    content_type = models.ForeignKey(
        ContentType,
        models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_("Content type"),
    )

    class Meta:
        abstract = True
