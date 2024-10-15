from django.db import transaction

from db.music.models import Playlist, PlaylistTrack
from services.common import model_update

__all__ = [
    "playlist_create",
    "playlist_update",
    "playlist_destroy",
    "playlist_restore",
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


@transaction.atomic()
def playlist_restore(playlist_id):
    playlist = Playlist.all_objects.get(id=playlist_id)
    playlist.is_removed = False
    playlist.save(update_fields=["is_removed"])
    tracks = PlaylistTrack.all_objects.filter(playlist=playlist)
    for track in tracks:
        track.is_removed = False
    PlaylistTrack.all_objects.bulk_update(tracks, ("is_removed",))
    return playlist


def playlist_add_track(*, playlist_id, track_id):
    track_in_playlist = PlaylistTrack(playlist_id=playlist_id, track_id=track_id)
    track_in_playlist.full_clean()
    track_in_playlist.save()
    return track_in_playlist.track


def playlist_remove_track(*, playlist_id, track_id):
    PlaylistTrack.available_objects.get(
        playlist_id=playlist_id, track_id=track_id
    ).delete()
