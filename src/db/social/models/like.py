from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel
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

    class Meta(BaseModel.Meta):
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        constraints = [
            models.UniqueConstraint(fields=("owner", "target_id"), name="unique_like"),
        ]
