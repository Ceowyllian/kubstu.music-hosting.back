from rest_framework import serializers

from api.common.serializers import DataObjectSerializer, ReadOnlyMixin
from db.music.models import GENRE_CHOICES, Track

__all__ = [
    "TrackRetrieveSerializer",
    "TrackListSerializer",
    "TrackCreateSerializer",
    "TrackUpdateSerializer",
]


class TrackRetrieveSerializer(DataObjectSerializer, ReadOnlyMixin):
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


class TrackListSerializer(DataObjectSerializer, ReadOnlyMixin):
    class Meta(DataObjectSerializer.Meta):
        model = Track
        fields = DataObjectSerializer.Meta.fields + [
            "genre",
            "title",
            "duration",
            "release_date",
        ]


class TrackCreateSerializer(serializers.Serializer):
    sound_file = serializers.FileField()
    image = serializers.ImageField(
        required=False,
    )
    genre = serializers.ChoiceField(
        choices=GENRE_CHOICES,
        required=False,
    )
    title = serializers.CharField()
    description = serializers.CharField(
        required=False,
    )
    release_date = serializers.DateField(
        required=False,
    )


class TrackUpdateSerializer(serializers.Serializer):
    image = serializers.ImageField()
    genre = serializers.ChoiceField(
        choices=GENRE_CHOICES,
    )
    title = serializers.CharField()
    description = serializers.CharField()
    release_date = serializers.DateField()
