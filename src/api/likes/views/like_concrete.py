from api.likes.views.like_base import LikeView
from db.music.models import Album, Playlist, Track
from db.social.models import CommentBase

__all__ = [
    "TrackLikeView",
    "AlbumLikeView",
    "PlaylistLikeView",
    "CommentLikeView",
]


class TrackLikeView(LikeView):
    target_type = Track.like_target_type


class AlbumLikeView(LikeView):
    target_type = Album.like_target_type


class PlaylistLikeView(LikeView):
    target_type = Playlist.like_target_type


class CommentLikeView(LikeView):
    target_type = CommentBase.like_target_type
