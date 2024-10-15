from django.db import transaction

from db.music.models import Playlist, PlaylistTrack
from services.common import model_update

__all__ = [
    "playlist_create",
    "playlist_update",
    "playlist_destroy",
    "playlist_add_track",
    "playlist_remove_track",
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
    playlist.delete()
    playlist.tracks.all().delete()


def playlist_add_track(*, playlist_id, track_id):
    track_in_playlist = PlaylistTrack(playlist_id=playlist_id, track_id=track_id)
    track_in_playlist.full_clean()
    track_in_playlist.save()
    return track_in_playlist.track


def playlist_remove_track(*, playlist_id, track_id):
    PlaylistTrack.objects.get(playlist_id=playlist_id, track_id=track_id).delete()
