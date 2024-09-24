from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.music.views import AlbumViewSet, PlaylistViewSet, TrackViewSet

tracks_router = DefaultRouter()
tracks_router.register(r"tracks", TrackViewSet, "tracks")

playlist_router = DefaultRouter()
playlist_router.register(r"playlists", PlaylistViewSet, "playlists")

album_router = DefaultRouter()
album_router.register(r"albums", AlbumViewSet, "albums")

urlpatterns = [
    path(r"", include(tracks_router.urls)),
    path(r"", include(playlist_router.urls)),
    path(r"", include(album_router.urls)),
]
