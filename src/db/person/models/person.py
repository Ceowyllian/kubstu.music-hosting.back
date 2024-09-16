from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel

__all__ = [
    "Person",
]

User = get_user_model()


class Person(BaseModel):

    user = models.OneToOneField(
        to=User,
        editable=False,
        on_delete=models.RESTRICT,
        verbose_name=_("User"),
    )
    avatar = models.ImageField(
        upload_to="avatars",
        null=True,
        blank=True,
        editable=True,
        verbose_name=_("Avatar"),
    )
    summary = models.CharField(
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
        related_name="followers",
        related_query_name="follower",
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
