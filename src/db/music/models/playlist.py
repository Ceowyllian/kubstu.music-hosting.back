from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common.models import BaseModel
from db.person.models import WithOwnerMixin
from db.social import with_likes
from db.social.models import LIKE_TARGET_TYPE_CHOICES

__all__ = [
    "Playlist",
]


@with_likes(LIKE_TARGET_TYPE_CHOICES.Playlist)
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
        through="music.PlaylistTrack",
        through_fields=("playlist", "track"),
        verbose_name=_("Tracks"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")
