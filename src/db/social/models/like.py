from django.utils.translation import gettext_lazy as _

from db.social.models.base import LikeBase, make_target_field

__all__ = [
    "TrackLike",
    "PlaylistLike",
    "AlbumLike",
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


class AlbumLike(LikeBase):
    target = make_target_field("music.Album")

    class Meta(LikeBase.Meta):
        verbose_name = _("Album like")
        verbose_name_plural = _("Album likes")
