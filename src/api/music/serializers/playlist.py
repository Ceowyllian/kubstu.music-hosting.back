from django.utils.translation import gettext_lazy as _

from api.common import DataObjectSerializer, EmptySerializer, ReadOnlyMixin, fields
from api.music.serializers.track import TrackListSerializer
from db.music.models import Playlist

__all__ = [
    "PlaylistSerializer",
    "PlaylistWithTracksSerializer",
    "PlaylistCreateSerializer",
    "PlaylistUpdateSerializer",
]


class PlaylistSerializer(
    DataObjectSerializer,
    ReadOnlyMixin,
):
    class Meta(DataObjectSerializer.Meta):
        model = Playlist
        fields = DataObjectSerializer.Meta.fields + [
            "name",
        ]


class PlaylistWithTracksSerializer(
    DataObjectSerializer,
    ReadOnlyMixin,
):
    tracks = fields.ListField(
        child=TrackListSerializer(),
        help_text=_("Tracks"),
    )

    class Meta(DataObjectSerializer.Meta):
        model = Playlist
        fields = DataObjectSerializer.Meta.fields + [
            "name",
            "tracks",
        ]


class PlaylistCreateSerializer(EmptySerializer):
    name = fields.CharField(
        help_text=_("Playlist name"),
    )
    track_ids = fields.ListField(
        child=fields.UUIDField(),
        allow_null=False,
        allow_empty=False,
        required=False,
        help_text=_("Track IDs"),
    )


class PlaylistUpdateSerializer(EmptySerializer):
    name = fields.CharField(
        help_text=_("Playlist name"),
    )
