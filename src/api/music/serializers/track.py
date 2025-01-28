from api.common import DataObjectSerializer, EmptySerializer, PersonSerializer, fields
from db.music.models import GENRE_CHOICES, Track

__all__ = [
    "TrackRetrieveSerializer",
    "TrackListSerializer",
    "TrackCreateSerializer",
    "TrackUpdateSerializer",
]


class TrackRetrieveSerializer(DataObjectSerializer):
    class Meta(DataObjectSerializer.Meta):
        model = Track
        fields = DataObjectSerializer.Meta.fields + [
            "sound_file",
            "image",
            "genre",
            "title",
            "description",
            "duration",
            "release_date",
        ]


class TrackListSerializer(DataObjectSerializer):
    owner = PersonSerializer()

    class Meta(DataObjectSerializer.Meta):
        model = Track
        fields = DataObjectSerializer.Meta.fields + [
            "image",
            "sound_file",
            "genre",
            "title",
            "duration",
            "release_date",
            "owner",
        ]


class TrackCreateSerializer(EmptySerializer):
    sound_file = fields.FileField()
    image = fields.ImageField(
        required=False,
    )
    genre = fields.ChoiceField(
        choices=GENRE_CHOICES,
        required=False,
    )
    title = fields.CharField()
    description = fields.CharField(
        required=False,
    )
    release_date = fields.DateField(
        required=False,
    )


class TrackUpdateSerializer(EmptySerializer):
    image = fields.ImageField()
    genre = fields.ChoiceField(
        choices=GENRE_CHOICES,
    )
    title = fields.CharField()
    description = fields.CharField()
    release_date = fields.DateField()
