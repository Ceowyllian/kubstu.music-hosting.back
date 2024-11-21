from api.common import DataObjectSerializer, EmptySerializer, fields
from db.music.models import Album, Playlist, Track
from db.person.models import Person

__all__ = [
    "PersonSearchSerializer",
    "TrackSearchSerializer",
    "PlaylistSearchSerializer",
    "SearchSerializer",
    "serialize_search_querysets",
]


class PersonSearchSerializer(DataObjectSerializer):
    username = fields.CharField(
        source="user__username",
    )

    class Meta(DataObjectSerializer.Meta):
        model = Person
        fields = DataObjectSerializer.Meta.fields + [
            "avatar",
            "user_id",
            "username",
        ]


class TrackSearchSerializer(DataObjectSerializer):
    owner = PersonSearchSerializer()

    class Meta(DataObjectSerializer.Meta):
        model = Track
        fields = DataObjectSerializer.Meta.fields + [
            "image",
            "genre",
            "title",
            "duration",
            "sound_file",
            "owner",
        ]


class PlaylistSearchSerializer(DataObjectSerializer):
    owner = PersonSearchSerializer()

    class Meta(DataObjectSerializer.Meta):
        model = Playlist
        fields = DataObjectSerializer.Meta.fields + [
            "name",
            "tracks",
            "owner",
        ]


class AlbumSearchSerializer(DataObjectSerializer):
    owner = PersonSearchSerializer()

    class Meta(DataObjectSerializer.Meta):
        model = Album
        fields = DataObjectSerializer.Meta.fields + [
            "image",
            "title",
            "release_date",
            "owner",
        ]


class SearchSerializer(EmptySerializer):
    track_list = TrackSearchSerializer(
        many=True,
    )
    album_list = AlbumSearchSerializer(
        many=True,
    )
    playlist_list = PlaylistSearchSerializer(
        many=True,
    )
    person_list = PersonSearchSerializer(
        many=True,
    )


def serialize_search_querysets(*querysets):
    serializer_mapping = {
        Track: TrackSearchSerializer,
        Album: AlbumSearchSerializer,
        Playlist: PlaylistSearchSerializer,
        Person: PersonSearchSerializer,
    }

    def key(qs):
        return qs.model._meta.model_name

    def serialize(qs):
        return serializer_mapping[qs.model](qs, many=True)

    return {key(qs): serialize(qs) for qs in querysets}
