from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common.models import BaseModel
from db.person.models import WithOwnerMixin

__all__ = [
    "Repost",
]


class Repost(BaseModel, WithOwnerMixin):
    target_id = models.UUIDField(
        null=False, blank=False, editable=False, verbose_name=_("Target ID")
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Repost")
        verbose_name_plural = _("Reposts")
        constraints = [
            models.UniqueConstraint(
                fields=("owner", "target_id"), name="unique_repost"
            ),
        ]
