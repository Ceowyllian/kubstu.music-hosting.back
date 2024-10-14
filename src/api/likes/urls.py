from django.urls import path

from api.likes.views import (
    AlbumLikeView,
    CommentLikeView,
    PlaylistLikeView,
    TrackLikeView,
)
from api.likes.views.like_base import LikeView


def like_url(prefix, view_class: type[LikeView]):
    return path(rf"{prefix}/<uuid:target_pk>/like/", view_class.as_view())


urlpatterns = [
    like_url("tracks", TrackLikeView),
    like_url("comments", CommentLikeView),
    like_url("playlists", PlaylistLikeView),
    like_url("albums", AlbumLikeView),
]
