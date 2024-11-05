from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.comments.views import (
    AlbumCommentsView,
    CommentsNestedView,
    PlaylistCommentsView,
    TrackCommentsView,
)


def comment_url(prefix, view_class: type[CommentsNestedView], target_name):
    router = DefaultRouter()
    router.register("comments", view_class, f"{target_name}-comments")
    return path(rf"{prefix}/<uuid:target_pK>/", include(router.urls))


urlpatterns = [
    comment_url("music/tracks", TrackCommentsView, "track"),
    comment_url("music/playlists", PlaylistCommentsView, "playlist"),
    comment_url("music/albums", AlbumCommentsView, "album"),
]
