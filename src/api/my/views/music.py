from api.common import SCHEMA_TAG_MY, IsAuthenticated, extend_schema
from api.music.views import AlbumListView, PlaylistListView, TrackListView
from db.music.models import Album, Playlist, Track

__all__ = [
    "MyTracksView",
    "MyPlaylistsView",
    "MyAlbumsView",
]


@extend_schema(tags=[SCHEMA_TAG_MY])
class MyTracksView(TrackListView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Track.objects.filter(owner=self.request.user.person)


@extend_schema(tags=[SCHEMA_TAG_MY])
class MyPlaylistsView(PlaylistListView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(owner=self.request.user.person)


@extend_schema(tags=[SCHEMA_TAG_MY])
class MyAlbumsView(AlbumListView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user.person)
