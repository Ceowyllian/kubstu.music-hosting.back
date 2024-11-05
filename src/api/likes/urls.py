from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.likes.views import (
    AlbumLikeView,
    CommentLikeView,
    PlaylistLikeView,
    TrackLikeView,
)
from api.likes.views.like_base import LikeView


def like_url(prefix, view_class: type[LikeView], target_name):
    router = DefaultRouter()
    router.register("like", view_class, f"{target_name}-likes")
    return path(rf"{prefix}/<uuid:target_pk>/", include(router.urls))


urlpatterns = [
    like_url("music/tracks", TrackLikeView, "track"),
    like_url("social/comments", CommentLikeView, "comment"),
    like_url("music/playlists", PlaylistLikeView, "playlist"),
    like_url("music/albums", AlbumLikeView, "album"),
]
