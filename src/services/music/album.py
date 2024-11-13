from django.db import transaction

from db.music.models import Album
from services.common import model_update
from services.music.track_collection import TrackCollectionService

__all__ = [
    "album_create",
    "album_update",
    "album_destroy",
]


def album_create(*, user, image, title, description, release_date):
    album = Album(
        owner=user.person,
        image=image,
        title=title,
        description=description,
        release_date=release_date,
    )
    album.full_clean()
    album.save()
    return album


def album_update(album, **data):
    album, _ = model_update(
        instance=album,
        fields=["image", "title", "description", "release_date"],
        data=data,
    )
    return album


@transaction.atomic()
def album_destroy(album: Album):
    TrackCollectionService(album).items_qs.delete()
    album.delete()
