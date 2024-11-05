from api.comments.views.comment_nested_view_base import CommentsNestedView
from db.music.models import Album, Playlist, Track

__all__ = [
    "TrackCommentsView",
    "AlbumCommentsView",
    "PlaylistCommentsView",
]


class TrackCommentsView(CommentsNestedView):
    target_model_class = Track


class AlbumCommentsView(CommentsNestedView):
    target_model_class = Album


class PlaylistCommentsView(CommentsNestedView):
    target_model_class = Playlist
