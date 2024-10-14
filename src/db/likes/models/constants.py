from model_utils import Choices

__all__ = [
    "LIKE_TARGET_TYPE_CHOICES",
]

LIKE_TARGET_TYPE_CHOICES = Choices(
    (0, "Track", "Track"),
    (1, "Album", "Album"),
    (2, "Playlist", "Playlist"),
    (3, "Comment", "Comment"),
)
