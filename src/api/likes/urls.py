from api.likes.views import (
    AlbumLikeView,
    CommentLikeView,
    PlaylistLikeView,
    TrackLikeView,
)
from api.social.urls import like_url

urlpatterns = [
    like_url("music/tracks", TrackLikeView, "track"),
    like_url("comments", CommentLikeView, "comment"),
    like_url("music/playlists", PlaylistLikeView, "playlist"),
    like_url("music/albums", AlbumLikeView, "album"),
]
