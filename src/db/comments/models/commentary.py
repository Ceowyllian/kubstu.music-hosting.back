from django.db import models
from django.utils.translation import gettext_lazy as _

from db.comments.models.constants import COMMENT_STATUS_CHOICES
from db.common import BaseModel
from db.likes import with_likes
from db.likes.models.constants import LIKE_TARGET_TYPE_CHOICES
from db.person.models import WithOwnerMixin

__all__ = [
    "Comment",
]


@with_likes(LIKE_TARGET_TYPE_CHOICES.Comment)
class Comment(BaseModel, WithOwnerMixin):
    target_id = models.UUIDField(
        blank=False,
        null=False,
        editable=False,
        verbose_name=_("Target ID"),
    )

    subject = models.TextField(
        blank=False,
        null=False,
        editable=True,
        verbose_name=_("Subject"),
    )
    parent = models.ForeignKey(
        to="self",
        on_delete=models.RESTRICT,
        related_name="children",
        null=True,
        blank=True,
        verbose_name=_("Parent comment"),
    )
    status = models.PositiveIntegerField(
        blank=False,
        null=False,
        editable=True,
        default=COMMENT_STATUS_CHOICES.Visible,
        choices=COMMENT_STATUS_CHOICES,
        verbose_name=_("Comment status"),
    )

    def __str__(self):
        return f"{self.owner.username} - {self.subject}"

    class Meta(BaseModel.Meta):
        verbose_name = _("Commentary")
        verbose_name_plural = _("Commentaries")