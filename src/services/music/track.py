from datetime import date
from typing import Any, TypedDict

from django.db import transaction

from db.likes.models import Like
from db.music.models import AlbumTrack, PlaylistTrack, Track
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
    # TODO determine duration
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


def track_update(*, track: Track, data: TrackUpdateFields):
    instance, _ = model_update(
        instance=track,
        fields=["image", "genre", "title", "description", "release_date"],
        data=data,
    )
    return instance


def track_delete(instance: Track):
    track_likes = Like.objects.filter(target_id=instance.id)
    track_in_albums = AlbumTrack.objects.filter(track=instance)
    track_in_playlists = PlaylistTrack.objects.filter(track=instance)
    with transaction.atomic():
        instance.comments.all().delete()
        track_likes.delete()
        track_in_albums.delete()
        track_in_playlists.delete()
        instance.delete()
