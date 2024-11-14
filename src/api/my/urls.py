from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.my.views import MyAlbumsView, MyPlaylistsView, MyTracksView

router = DefaultRouter()
router.register("tracks", MyTracksView, "my-tracks")
router.register("playlists", MyPlaylistsView, "my-playlists")
router.register("albums", MyAlbumsView, "my-albums")

urlpatterns = [
    path("", include(router.urls)),
]
