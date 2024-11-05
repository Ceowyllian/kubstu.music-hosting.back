from django.db import models
from django.utils.translation import gettext_lazy as _

from db.comments.models import WithCommentsMixin
from db.likes.models import WithLikesMixin
from db.music.models.track_collection import TrackCollection
from db.person.models import WithOwnerMixin

__all__ = [
    "Playlist",
]


class Playlist(
    TrackCollection,
    WithOwnerMixin,
    WithLikesMixin,
    WithCommentsMixin,
):
    name = models.TextField(
        blank=False,
        null=False,
        editable=True,
        verbose_name=_("Name"),
    )
    tracks = TrackCollection.Items("music.PlaylistTrack")

    def __str__(self):
        return self.name

    class Meta(TrackCollection.Meta):
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")
