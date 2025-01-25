from uuid import uuid4

import soundfile as sf
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from db.comments.models import WithCommentsMixin
from db.common import BaseModel
from db.likes.models import WithLikesMixin
from db.music.models.constants import GENRE_CHOICES
from db.person.models import WithOwnerMixin

__all__ = [
    "Track",
]


def sound_file_path(instance, _):
    with sf.SoundFile(instance.sound_file, "rb") as f:
        extension = f.format
    return f"tracks/{uuid4()}.{extension}"


def image_path(instance, _):
    with Image.open(instance.avatar) as im:
        extension = im.format
    return f"track_images/{uuid4()}.{extension}"


class Track(
    BaseModel,
    WithOwnerMixin,
    WithLikesMixin,
    WithCommentsMixin,
):

    sound_file = models.FileField(
        upload_to=sound_file_path,
        blank=False,
        editable=False,
        null=False,
        verbose_name=_("Sound file"),
    )
    image = models.ImageField(
        upload_to=image_path,
        null=True,
        blank=True,
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
