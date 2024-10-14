from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel
from db.likes.models.constants import LIKE_TARGET_TYPE_CHOICES
from db.person.models import WithOwnerMixin

__all__ = [
    "Like",
]


class Like(BaseModel, WithOwnerMixin):
    target_id = models.UUIDField(
        null=False,
        blank=False,
        editable=False,
        verbose_name=_("Target ID"),
    )
    target_type = models.PositiveIntegerField(
        null=False,
        blank=False,
        editable=False,
        choices=LIKE_TARGET_TYPE_CHOICES,
        verbose_name=_("Target model type"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        constraints = [
            models.UniqueConstraint(fields=("owner", "target_id"), name="unique_like"),
        ]
