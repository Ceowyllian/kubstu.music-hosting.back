from django.utils.translation import gettext_lazy as _

from db.social.models.base import RepostBase, make_target_field

__all__ = [
    "TrackRepost",
    "PlaylistRepost",
    "AlbumRepost",
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
