from django.db import transaction
from django.db.models import F, Max

from db.music.models import Track
from db.music.models.track_collection import TrackCollection, TrackCollectionItem

__all__ = [
    "collection_get_tracks",
    "collection_add_track",
    "collection_remove_track",
    "collection_swap_tracks",
]


def collection_get_tracks(collection: TrackCollection):
    items_model = collection.tracks.through
    return (
        items_model.objects.filter(parent=collection)
        .order_by("number")
        .values(
            "track__sound_file",
            "track__image",
            "track__genre",
            "track__title",
            "track__description",
            "track__duration",
            "track__release_date",
        )
    )


def collection_add_track(collection: TrackCollection, track_id: Track):
    item_model: type[TrackCollectionItem] = collection.tracks.through
    previous_number = item_model.objects.filter(parent=collection).aggregate(
        Max("number")
    )["number__max"]
    next_number = previous_number + 1 if previous_number else 0
    item = item_model(
        parent=collection,
        track_id=track_id,
        number=next_number,
    )
    item.full_clean()
    item.save()


@transaction.atomic()
def collection_remove_track(collection: TrackCollection, track_id):
    item_model: type[TrackCollectionItem] = collection.tracks.through
    item = item_model.objects.get(parent=collection, track_id=track_id)
    item_model.objects.filter(parent=collection, number__gt=item.number).update(
        number=F("number") - 1
    )
    item.delete()


def collection_swap_tracks(collection, left_id, right_id):
    item_model: type[TrackCollectionItem] = collection.tracks.through
    left_item = item_model.objects.get(parent=collection, track_id=left_id)
    right_item = item_model.objects.get(parent=collection, track_id=right_id)
    left_item.number, right_item.number = right_item.number, left_item.number
    left_item.save(update_fields=["number"])
    right_item.save(update_fields=["number"])
    return right_item, left_item
