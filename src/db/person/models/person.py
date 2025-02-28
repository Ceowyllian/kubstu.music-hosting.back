from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from db.common import BaseModel

__all__ = [
    "Person",
]

User = get_user_model()


def avatar_path(instance, _):
    with Image.open(instance.avatar) as im:
        extension = im.format
    return f"avatars/{uuid4()}.{extension}"


class Person(BaseModel):

    user = models.OneToOneField(
        to=User,
        editable=False,
        on_delete=models.RESTRICT,
        verbose_name=_("User"),
    )
    avatar = models.ImageField(
        upload_to=avatar_path,
        null=True,
        blank=True,
        editable=True,
        verbose_name=_("Avatar"),
    )
    summary = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Summary"),
    )
    public_email = models.EmailField(
        null=True,
        blank=True,
        editable=True,
        verbose_name=_("Public email"),
    )
    saved_playlists = models.ManyToManyField(
        to="music.Playlist",
        through="person.SavedPlaylist",
        through_fields=("owner", "playlist"),
    )
    subscribers = models.ManyToManyField(
        to="self",
        related_query_name="subscriber",
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")
