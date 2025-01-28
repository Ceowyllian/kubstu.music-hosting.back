from django.db import transaction
from django.db.models import Count

from db.music.models import Playlist
from services.common import model_update
from services.music.track_collection import TrackCollectionService

__all__ = [
    "playlist_create",
    "playlist_update",
    "playlist_destroy",
    "playlist_list",
]


def playlist_create(
    *,
    user,
    name,
):
    playlist = Playlist(
        name=name,
        owner=user.person,
    )
    playlist.full_clean()
    playlist.save()
    return playlist


def playlist_update(*, playlist: Playlist, name: str):
    model_update(instance=playlist, fields=("name",), data={"name": name})
    return playlist


@transaction.atomic()
def playlist_destroy(playlist: Playlist):
    TrackCollectionService(playlist).items_qs.delete()
    playlist.delete()


def playlist_list():
    return Playlist.objects.annotate(total_tracks=Count("playlisttrack"))
