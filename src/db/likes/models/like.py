from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel, WithSocialTargetMixin
from db.person.models import WithOwnerMixin

__all__ = [
    "Like",
]


class Like(
    BaseModel,
    WithOwnerMixin,
    WithSocialTargetMixin,
):
    class Meta(BaseModel.Meta):
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        constraints = [
            models.UniqueConstraint(fields=("owner", "target_id"), name="unique_like"),
        ]
