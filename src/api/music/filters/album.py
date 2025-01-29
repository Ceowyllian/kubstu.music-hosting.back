from api.common import FilterSet, base_model_fields, filter_fields, owner_fields
from db.music.models import Album

__all__ = [
    "AlbumFilterSet",
]


class AlbumFilterSet(FilterSet):
    exclude_track_id = filter_fields.UUIDFilter(
        method="filter_exclude_track_id",
    )

    def filter_exclude_track_id(self, queryset, _, value):
        return queryset.exclude(albumtrack__track__id=value)

    class Meta:
        model = Album
        fields = {
            **base_model_fields,
            **owner_fields,
            "release_date": [
                "exact",
                "lt",
                "gt",
                "year__exact",
                "year__lt",
                "year__gt",
            ],
        }
