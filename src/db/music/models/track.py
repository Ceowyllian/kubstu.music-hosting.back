from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel
from db.music.models.constants import GENRE_CHOICES

__all__ = [
    "Track",
]


class Track(BaseModel):

    sound_file = models.FileField(
        upload_to="tracks",
        blank=False,
        editable=False,
        null=False,
        verbose_name=_("Sound file"),
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="tracks_images",
        verbose_name=_("Image"),
    )
    genre = models.IntegerField(
        blank=True,
        null=True,
        choices=GENRE_CHOICES,
        verbose_name=_("Genre"),
    )
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("Song title"),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Song description"),
    )
    duration = models.DurationField(
        blank=False,
        null=False,
        editable=False,
        verbose_name=_("Duration"),
    )
    release_date = models.DateField(
        blank=True,
        null=True,
        editable=True,
        verbose_name=_("Release date"),
    )
    uploaded_by = models.ForeignKey(
        "social.Person",
        on_delete=models.RESTRICT,
        blank=False,
        null=False,
        editable=False,
        related_name="uploaded_tracks",
        related_query_name="uploaded_track",
        verbose_name=_("Uploaded by"),
    )

    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
