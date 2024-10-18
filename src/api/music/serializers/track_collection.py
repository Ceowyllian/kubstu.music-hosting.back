from django.utils.translation import gettext_lazy as _

from api.common import EmptySerializer, fields

__all__ = [
    "CollectionAddTrackSerializer",
    "CollectionSwapTracksSerializer",
]


class CollectionAddTrackSerializer(EmptySerializer):
    track_id = fields.UUIDField(
        label=_("Track ID"),
    )


class CollectionSwapTracksSerializer(EmptySerializer):
    left_id = fields.UUIDField(
        label=_("Track ID"),
    )
    right_id = fields.UUIDField(
        label=_("Track ID"),
    )
