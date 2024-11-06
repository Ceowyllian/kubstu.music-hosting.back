from api.likes.views.like_base import LikeView
from db.comments.models import Comment
from db.music.models import Album, Playlist, Track

__all__ = [
    "TrackLikeView",
    "AlbumLikeView",
    "PlaylistLikeView",
    "CommentLikeView",
]


class TrackLikeView(LikeView):
    def get_target_model_class(self):
        return Track


class AlbumLikeView(LikeView):
    def get_target_model_class(self):
        return Album


class PlaylistLikeView(LikeView):
    def get_target_model_class(self):
        return Playlist


class CommentLikeView(LikeView):
    def get_target_model_class(self):
        return Comment
