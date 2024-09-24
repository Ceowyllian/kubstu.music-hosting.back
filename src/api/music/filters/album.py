from api.common import FilterSet, base_model_fields, owner_fields
from db.music.models import Album

__all__ = [
    "AlbumFilterSet",
]


class AlbumFilterSet(FilterSet):
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
