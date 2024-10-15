from django.utils.translation import gettext_lazy as _

from db.music.models.track_collection import TrackCollectionItem

__all__ = [
    "PlaylistTrack",
    "AlbumTrack",
]


class PlaylistTrack(TrackCollectionItem):
    parent = TrackCollectionItem.Parent("music.Playlist")

    class Meta(TrackCollectionItem.Meta):
        verbose_name = _("Playlist track")
        verbose_name_plural = _("Playlist tracks")


class AlbumTrack(TrackCollectionItem):
    parent = TrackCollectionItem.Parent("music.Album")

    class Meta(TrackCollectionItem.Meta):
        verbose_name = _("Album track")
        verbose_name_plural = _("Album tracks")
