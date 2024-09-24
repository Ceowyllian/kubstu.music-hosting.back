from api.common import FilterSet, base_model_fields, filter_fields, owner_fields
from db.music.models import GENRE_CHOICES, Track

__all__ = [
    "TrackFilterSet",
]


class TrackFilterSet(FilterSet):
    genre = filter_fields.ChoiceFilter(
        choices=GENRE_CHOICES,
        null_value=None,
    )

    class Meta:
        model = Track
        fields = {
            **base_model_fields,
            **owner_fields,
            "genre": ["exact"],
            "duration": ["exact", "lt", "gt"],
            "release_date": [
                "exact",
                "lt",
                "gt",
                "year__exact",
                "year__lt",
                "year__gt",
            ],
        }
