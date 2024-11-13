from django.db import transaction

from db.music.models import Playlist
from services.common import model_update

__all__ = [
    "playlist_create",
    "playlist_update",
    "playlist_destroy",
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
