from api.common import FilterSet, base_model_fields, owner_fields
from db.music.models import Playlist

__all__ = [
    "PlaylistFilterSet",
]


class PlaylistFilterSet(FilterSet):
    class Meta:
        model = Playlist
        fields = {
            **base_model_fields,
            **owner_fields,
            "tracks__id": ["exact"],
        }
