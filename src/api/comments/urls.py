from api.comments.views import (
    AlbumCommentsView,
    PlaylistCommentsView,
    TrackCommentsView,
)
from api.social.urls import comments_url

urlpatterns = [
    comments_url("music/tracks", TrackCommentsView, "track"),
    comments_url("music/playlists", PlaylistCommentsView, "playlist"),
    comments_url("music/albums", AlbumCommentsView, "album"),
]
