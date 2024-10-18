from django.db import transaction
from django.db.models import F, Max, QuerySet

from db.music.models import Track
from db.music.models.track_collection import TrackCollection, TrackCollectionItem

__all__ = [
    "TrackCollectionService",
]


class TrackCollectionService:

    def __init__(self, collection):
        self.collection_class: type[TrackCollection] = collection._meta.model
        self.collection: TrackCollection = collection
        self.item_class: type[TrackCollectionItem] = (
            self.collection_class.tracks.through
        )
        self.item_field_name: str = self.item_class._meta.model_name

    @property
    def tracks_qs(self) -> QuerySet[Track]:
        return self.collection.tracks.order_by(f"{self.item_field_name}__number")

    @property
    def items_qs(self) -> QuerySet[TrackCollectionItem]:
        return self.item_class.objects.filter(parent=self.collection)

    def get_item(self, track_id):
        return self.items_qs.get(track_id=track_id)

    def get_count(self) -> int:
        return self.items_qs.aggregate(Max("number"))["number__max"]

    def add_track(self, track_id: Track):
        item = self.item_class(
            parent=self.collection,
            track_id=track_id,
            number=self.get_count() + 1,
        )
        item.full_clean()
        item.save()
        return item

    @transaction.atomic()
    def remove_track(self, track_id: Track):
        item = self.get_item(track_id)
        removed_at = item.number
        self.items_qs.filter(number__gt=removed_at).update(number=F("number") - 1)
        item.delete()

    @transaction.atomic()
    def swap_tracks(self, left_id, right_id):
        left = self.get_item(left_id)
        right = self.get_item(right_id)
        left.number, right.number = right.number, left.number
        left.save(update_fields=["number"])
        right.save(update_fields=["number"])
        return right, left
