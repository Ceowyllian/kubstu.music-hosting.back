from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from api.music.views import (
    AlbumTrackViewSet,
    AlbumViewSet,
    PlaylistTrackViewSet,
    PlaylistViewSet,
    TrackViewSet,
)

tracks_router = DefaultRouter()
tracks_router.register(r"tracks", TrackViewSet, "tracks")

playlist_router = DefaultRouter()
playlist_router.register(r"playlists", PlaylistViewSet, "playlists")

album_router = DefaultRouter()
album_router.register(r"albums", AlbumViewSet, "albums")

playlist_tracks_router = NestedDefaultRouter(
    playlist_router, r"playlists", lookup="parent"
)
playlist_tracks_router.register(r"tracks", PlaylistTrackViewSet, "playlist-tracks")

album_tracks_router = NestedDefaultRouter(album_router, r"albums", lookup="parent")
album_tracks_router.register(r"tracks", AlbumTrackViewSet, "album-tracks")

urlpatterns = [
    path(r"", include(tracks_router.urls)),
    path(r"", include(playlist_router.urls)),
    path(r"", include(album_router.urls)),
    path(r"", include(playlist_tracks_router.urls)),
    path(r"", include(album_tracks_router.urls)),
]
