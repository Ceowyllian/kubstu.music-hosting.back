from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common.models import BaseModel

__all__ = [
    "Playlist",
]

from db.social.models import WithOwnerMixin


class Playlist(
    BaseModel,
    WithOwnerMixin,
):
    name = models.TextField(
        blank=False,
        null=False,
        editable=True,
        verbose_name=_("Name"),
    )
    tracks = models.ManyToManyField(
        to="music.Track",
        related_name=_("playlists"),
        verbose_name=_("Tracks"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")
