from django.db import models
from django.utils.decorators import classonlymethod
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel

__all__ = [
    "TrackCollection",
    "TrackCollectionItem",
]


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

    @classonlymethod
    def Parent(cls, to: str):
        return models.ForeignKey(
            to, on_delete=models.RESTRICT, verbose_name=_(to.split(".")[-1])
        )

    class Meta(BaseModel.Meta):
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=("parent", "track"), name="unique_%(class)s"
            ),
        ]


class TrackCollection(BaseModel):
    tracks = NotImplemented

    @classonlymethod
    def Items(cls, through: str):
        return models.ManyToManyField(
            "music.Track",
            related_name=_(f"{cls.__name__.lower()}s"),
            through=through,
            through_fields=("parent", "track"),
            verbose_name=_("Tracks"),
        )

    class Meta(BaseModel.Meta):
        abstract = True
