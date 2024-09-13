from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common.models import BaseModel
from db.social.models import WithOwnerMixin
from db.social.models.base import make_target_field


class RepostBase(
    BaseModel,
    WithOwnerMixin,
):
    target: type[models.Model] = None

    class Meta(BaseModel.Meta):
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=("owner", "target"), name="unique_%(class)s"
            ),
        ]


class TrackRepost(RepostBase):
    target = make_target_field("music.Track")

    class Meta(RepostBase.Meta):
        verbose_name = _("Track repost")
        verbose_name_plural = _("Track reposts")


class PlaylistRepost(RepostBase):
    target = make_target_field("music.Playlist")

    class Meta(RepostBase.Meta):
        verbose_name = _("Playlist repost")
        verbose_name_plural = _("Playlist reposts")


class AlbumRepost(RepostBase):
    target = make_target_field("music.Album")

    class Meta(RepostBase.Meta):
        verbose_name = _("Album repost")
        verbose_name_plural = _("Album reposts")
