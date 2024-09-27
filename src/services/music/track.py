from datetime import date
from typing import Any, TypedDict

from django.db import transaction

from db.music.models import Album, Playlist, Track
from db.social.models import TrackLike
from services.common import model_update

__all__ = [
    "track_create",
    "track_update",
    "track_delete",
]


def track_create(
    *,
    user,
    sound_file,
    image,
    genre,
    title,
    description,
    release_date,
):
    track = Track(
        owner=user.person,
        sound_file=sound_file,
        image=image,
        genre=genre,
        title=title,
        description=description,
        release_date=release_date,
    )
    track.full_clean()
    track.save()
    return track


class TrackUpdateFields(TypedDict):
    image: Any
    genre: int
    title: str
    description: str
    release_date: date


def track_update(*, track_id, data: TrackUpdateFields):
    model_update(
        instance=Track.objects.select_for_update().get(id=track_id),
        fields=["image", "genre", "title", "description", "release_date"],
        data=data,
    )


def track_delete(instance: Track):
    likes = TrackLike.objects.filter(target=instance)
    albums = Album.objects.filter(tracks__id=instance.id)
    playlists = Playlist.objects.filter(tracks__id=instance.id)
    with transaction.atomic():
        likes.delete()
        for album in albums:
            album.tracks.remove(instance)
        for playlist in playlists:
            playlist.tracks.remove(instance)
        instance.delete()
