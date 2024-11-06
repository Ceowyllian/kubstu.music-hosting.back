from api.comments.views.comments_base import CommentsNestedView
from db.music.models import Album, Playlist, Track

__all__ = [
    "TrackCommentsView",
    "AlbumCommentsView",
    "PlaylistCommentsView",
]


class TrackCommentsView(CommentsNestedView):
    def get_target_model_class(self):
        return Track


class AlbumCommentsView(CommentsNestedView):
    def get_target_model_class(self):
        return Album


class PlaylistCommentsView(CommentsNestedView):
    def get_target_model_class(self):
        return Playlist
