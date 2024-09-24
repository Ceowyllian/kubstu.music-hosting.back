from django.utils.translation import gettext_lazy as _

from api.common import DataObjectSerializer, EmptySerializer, fields
from api.music.serializers.track import TrackListSerializer
from db.music.models import Album

__all__ = [
    "AlbumCreateSerializer",
    "AlbumSerializer",
    "AlbumUpdateSerializer",
    "AlbumWithTracksSerializer",
]


class AlbumSerializer(DataObjectSerializer):
    class Meta(DataObjectSerializer.Meta):
        model = Album
        fields = DataObjectSerializer.Meta.fields + [
            "title",
            "description",
            "release_date",
        ]


class AlbumWithTracksSerializer(DataObjectSerializer):
    tracks = fields.ListField(
        child=TrackListSerializer(),
        help_text=_("Tracks"),
    )

    class Meta(DataObjectSerializer):
        model = Album
        fields = DataObjectSerializer.Meta.fields + [
            "title",
            "description",
            "release_date",
            "tracks",
        ]


class AlbumCreateSerializer(EmptySerializer):
    title = fields.CharField(
        allow_null=False,
        allow_blank=False,
        help_text=_("Album title"),
    )
    description = fields.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        help_text=_("Album description"),
    )
    release_date = fields.DateField(
        required=False,
        allow_null=True,
        help_text=_("ReleaseDate"),
    )
    track_ids = fields.ListField(
        child=fields.UUIDField(),
        allow_null=False,
        allow_empty=False,
        required=False,
        help_text=_("Track IDs"),
    )


class AlbumUpdateSerializer(EmptySerializer):
    title = fields.CharField(
        allow_null=False,
        allow_blank=False,
        help_text=_("Album title"),
    )
    description = fields.CharField(
        allow_null=True,
        allow_blank=False,
        help_text=_("Album description"),
    )
    release_date = fields.DateField(
        allow_null=True,
        help_text=_("Help text"),
    )
