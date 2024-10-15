from django.utils.translation import gettext_lazy as _

from api.common import DataObjectSerializer, EmptySerializer, fields
from api.music.serializers.track import TrackListSerializer
from db.music.models import Playlist

__all__ = [
    "PlaylistSerializer",
    "PlaylistWithTracksSerializer",
    "PlaylistCreateSerializer",
    "PlaylistUpdateSerializer",
    "PlaylistAddTrackSerializer",
]


class PlaylistSerializer(DataObjectSerializer):
    class Meta(DataObjectSerializer.Meta):
        model = Playlist
        fields = DataObjectSerializer.Meta.fields + [
            "name",
        ]


class PlaylistWithTracksSerializer(DataObjectSerializer):
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


class PlaylistUpdateSerializer(EmptySerializer):
    name = fields.CharField(
        help_text=_("Playlist name"),
    )


class PlaylistAddTrackSerializer(EmptySerializer):
    track_id = fields.UUIDField(
        help_text=_("Track ID"),
    )
