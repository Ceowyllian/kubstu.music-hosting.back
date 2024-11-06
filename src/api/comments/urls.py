from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.comments.views import (
    AlbumCommentsView,
    CommentsView,
    PlaylistCommentsView,
    TrackCommentsView,
)
from api.social.urls import comments_url

router = DefaultRouter()
router.register(r"", CommentsView, "comments")

urlpatterns = [
    comments_url("music/tracks", TrackCommentsView, "track"),
    comments_url("music/playlists", PlaylistCommentsView, "playlist"),
    comments_url("music/albums", AlbumCommentsView, "album"),
    path(r"comments/", include(router.urls)),
]
