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
    queryset = Track.objects.all()


class AlbumLikeView(LikeView):
    queryset = Album.objects.all()


class PlaylistLikeView(LikeView):
    queryset = Playlist.objects.all()


class CommentLikeView(LikeView):
    queryset = Comment.objects.all()
