from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel
from db.person.models.owner_mixin import WithOwnerMixin

__all__ = [
    "SavedPlaylist",
]


class SavedPlaylist(
    BaseModel,
    WithOwnerMixin,
):
    playlist = models.ForeignKey(
        "music.Playlist",
        on_delete=models.RESTRICT,
        verbose_name=_("Playlist"),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Saved playlist")
        verbose_name_plural = _("Saved playlists")
        constraints = [
            models.UniqueConstraint(
                fields=("owner", "playlist"), name="unique_%(class)s"
            ),
        ]
