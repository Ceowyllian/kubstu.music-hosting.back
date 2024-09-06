from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel

__all__ = [
    "TrackLike",
]


class TrackLike(BaseModel):

    liked_by = models.ForeignKey(
        to="social.Person",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_("Liked by"),
    )
    track = models.ForeignKey(
        to="music.Track",
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_("Track"),
    )

    class Meta:
        verbose_name = _("Track like")
        verbose_name_plural = _("Track likes")
        constraints = [
            models.UniqueConstraint(
                fields=("liked_by", "track"),
                name="unique_track_liking",
            ),
        ]
