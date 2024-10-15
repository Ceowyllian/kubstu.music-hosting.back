from django.db import models
from django.utils.translation import gettext_lazy as _

from db.likes import with_likes
from db.likes.models.constants import LIKE_TARGET_TYPE_CHOICES
from db.music.models.track_collection import TrackCollection
from db.person.models import WithOwnerMixin

__all__ = [
    "Album",
]


@with_likes(LIKE_TARGET_TYPE_CHOICES.Album)
class Album(
    TrackCollection,
    WithOwnerMixin,
):
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="albums_images",
        verbose_name=_("Image"),
    )
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
    tracks = TrackCollection.Items("music.AlbumTrack")

    def __str__(self):
        return self.title

    class Meta(TrackCollection.Meta):
        verbose_name = _("Album")
        verbose_name_plural = _("Playlists")
