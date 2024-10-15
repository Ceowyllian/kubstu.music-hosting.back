from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from api.music.views import (
    AlbumViewSet,
    PlaylistTracksViewSet,
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
    playlist_router, r"playlists", lookup="playlist"
)
playlist_tracks_router.register(r"tracks", PlaylistTracksViewSet, "playlist-tracks")

urlpatterns = [
    path(r"", include(tracks_router.urls)),
    path(r"", include(playlist_router.urls)),
    path(r"", include(album_router.urls)),
    path(r"", include(playlist_tracks_router.urls)),
]
