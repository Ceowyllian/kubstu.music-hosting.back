from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel

__all__ = [
    "LikeBase",
    "TrackLike",
    "PlaylistLike",
]

from db.social.models.base import make_target_field
from db.social.models.owner_mixin import WithOwnerMixin


class LikeBase(
    BaseModel,
    WithOwnerMixin,
):
    target: type[models.Model] = None

    class Meta(BaseModel.Meta):
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=("owner", "target"),
                name="unique_%(class)s",
            ),
        ]


class TrackLike(LikeBase):
    target = make_target_field("music.Track")

    class Meta(LikeBase.Meta):
        verbose_name = _("Track like")
        verbose_name_plural = _("Track likes")


class PlaylistLike(LikeBase):
    target = make_target_field("music.Playlist")

    class Meta(LikeBase.Meta):
        verbose_name = _("Playlist like")
        verbose_name_plural = _("Playlist likes")
