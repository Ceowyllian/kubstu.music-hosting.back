from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel
from db.social.models.base import make_target_field

__all__ = [
    "CommentBase",
    "TrackComment",
    "PlaylistComment",
]


class CommentBase(BaseModel):
    target: type[models.Model] = None
    author = models.ForeignKey(
        to="social.Person",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_("Author"),
    )

    class Meta(BaseModel.Meta):
        abstract = True


class TrackComment(CommentBase):
    target = make_target_field("music.Track")

    class Meta(CommentBase.Meta):
        verbose_name = _("Track comment")
        verbose_name_plural = _("Track comments")


class PlaylistComment(CommentBase):
    target = make_target_field("music.Playlist")

    class Meta(CommentBase.Meta):
        verbose_name = _("Playlist comment")
        verbose_name_plural = _("Playlist comments")
