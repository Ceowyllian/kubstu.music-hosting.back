from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel

__all__ = [
    "LikeBase",
    "TrackLike",
    "PlaylistLike",
]


def make_target_field(path_to_model: str):
    """
    :param path_to_model: should be a dotted path to django model "app_label.ModelClass"
    """
    model_name = path_to_model.split(".")[-1]
    return models.ForeignKey(
        to=model_name,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_(model_name),
    )


class LikeBase(BaseModel):
    target: type[models.Model] = None
    liked_by = models.ForeignKey(
        to="social.Person",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_("Liked by"),
    )

    class Meta(BaseModel.Meta):
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=("liked_by", "target"),
                name="unique_%(class)s",
            ),
        ]


class TrackLike(LikeBase):
    target = make_target_field("music.Track")

    class Meta(LikeBase.Meta):
        verbose_name = _("Track like")
        verbose_name_plural = _("Track likes")


class PlaylistLike(LikeBase):
    target = make_target_field("music.Playlist")

    class Meta(LikeBase.Meta):
        verbose_name = _("Playlist like")
        verbose_name_plural = _("Playlist likes")
