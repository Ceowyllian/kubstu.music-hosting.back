from api.common import FilterSet, base_model_fields, filter_fields, owner_fields
from db.music.models import Playlist

__all__ = [
    "PlaylistFilterSet",
]


class PlaylistFilterSet(FilterSet):
    exclude_track_id = filter_fields.UUIDFilter(
        method="filter_exclude_track_id",
    )

    def filter_exclude_track_id(self, queryset, _, value):
        return queryset.exclude(playlisttrack__track__id=value)

    class Meta:
        model = Playlist
        fields = {
            **base_model_fields,
            **owner_fields,
            "tracks__id": ["exact"],
        }
