from django.utils.translation import gettext_lazy as _

from db.comments.models.base import CommentBase, comment_target_field

__all__ = [
    "TrackComment",
    "PlaylistComment",
    "AlbumComment",
]


class TrackComment(CommentBase):
    target = comment_target_field("music.Track")

    class Meta(CommentBase.Meta):
        verbose_name = _("Track comment")
        verbose_name_plural = _("Track comments")


class PlaylistComment(CommentBase):
    target = comment_target_field("music.Playlist")

    class Meta(CommentBase.Meta):
        verbose_name = _("Playlist comment")
        verbose_name_plural = _("Playlist comments")


class AlbumComment(CommentBase):
    target = comment_target_field("music.Album")

    class Meta(CommentBase.Meta):
        verbose_name = _("Album comment")
        verbose_name_plural = _("Album comments")
