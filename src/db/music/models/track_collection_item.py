from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel


class TrackCollectionItem(BaseModel):
    parent = NotImplemented
    track = models.ForeignKey(
        "music.Track",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        verbose_name=_("Track"),
    )
    number = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name=_("Number in the list"),
    )

    class Meta(BaseModel.Meta):
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=("parent", "track"), name="unique_%(class)s"
            ),
        ]
