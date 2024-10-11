from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel
from db.person.models import WithOwnerMixin
from db.social import with_likes
from db.social.models.constants import LIKE_TARGET_TYPE_CHOICES

__all__ = [
    "Album",
]


@with_likes(LIKE_TARGET_TYPE_CHOICES.Album)
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
        through="music.AlbumTrack",
        through_fields=("album", "track"),
        verbose_name=_("Tracks"),
    )

    def __str__(self):
        return self.title

    class Meta(BaseModel.Meta):
        verbose_name = _("Album")
        verbose_name_plural = _("Playlists")
