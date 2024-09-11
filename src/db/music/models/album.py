from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel

__all__ = [
    "Album",
]

from db.social.models.owner_mixin import WithOwnerMixin


class Album(
    BaseModel,
    WithOwnerMixin,
):
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("Album title"),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Album description"),
    )
    release_date = models.DateField(
        blank=True,
        null=True,
        editable=True,
        verbose_name=_("Release date"),
    )
    tracks = models.ManyToManyField(
        to="music.Track",
        related_name=_("albums"),
        verbose_name=_("Tracks"),
    )

    def __str__(self):
        return self.title

    class Meta(BaseModel.Meta):
        verbose_name = _("Album")
        verbose_name_plural = _("Playlists")
