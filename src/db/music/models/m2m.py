from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common.models import BaseModel

__all__ = [
    "PlaylistTrack",
    "AlbumTrack",
]


class PlaylistTrack(BaseModel):
    playlist = models.ForeignKey(
        "music.Playlist",
        on_delete=models.RESTRICT,
        verbose_name=_("Playlist"),
    )
    track = models.ForeignKey(
        "music.Track",
        on_delete=models.RESTRICT,
        verbose_name=_("Track"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Playlist track")
        verbose_name_plural = _("Playlist tracks")
        constraints = [
            models.UniqueConstraint(
                fields=("playlist", "track"), name="unique_%(class)s"
            ),
        ]


class AlbumTrack(BaseModel):
    album = models.ForeignKey(
        "music.Album",
        on_delete=models.RESTRICT,
        verbose_name=_("Album"),
    )
    track = models.ForeignKey(
        "music.Track",
        on_delete=models.RESTRICT,
        verbose_name=_("Track"),
    )

    class Meta(BaseModel.Meta):
        constraints = [
            models.UniqueConstraint(fields=("album", "track"), name="unique_%(class)s"),
        ]
