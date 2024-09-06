from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common.models import BaseModel

__all__ = [
    "Playlist",
]


class Playlist(BaseModel):

    created_by = models.ForeignKey(
        "social.Person",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        related_name="created_playlists",
        related_query_name="created_playlist",
        verbose_name=_("Created by"),
    )
    name = models.TextField(
        blank=False,
        null=False,
        editable=True,
        verbose_name=_("Name"),
    )
    tracks = models.ManyToManyField(
        to="music.Track",
        verbose_name=_("Tracks"),
        related_name=_("playlists"),
    )

    class Meta:
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")
