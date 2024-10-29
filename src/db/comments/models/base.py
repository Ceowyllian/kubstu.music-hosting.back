from django.db import models
from django.utils.decorators import classonlymethod
from django.utils.functional import classproperty
from django.utils.translation import gettext_lazy as _

from db.comments.models.constants import COMMENT_STATUS_CHOICES
from db.common import BaseModel
from db.likes import with_likes
from db.likes.models.constants import LIKE_TARGET_TYPE_CHOICES
from db.person.models import WithOwnerMixin

__all__ = [
    "CommentBase",
    "comment_target_field",
]


def comment_target_field(model_label: str):
    model_name = model_label.split(".")[-1]
    return models.ForeignKey(
        to=model_label,
        on_delete=models.RESTRICT,
        related_name="comments",
        null=False,
        blank=False,
        editable=False,
        verbose_name=_(model_name),
    )


@with_likes(LIKE_TARGET_TYPE_CHOICES.Comment)
class CommentBase(BaseModel, WithOwnerMixin):
    target: models.ForeignKey = NotImplemented

    @classproperty
    @classonlymethod
    def target_model_class(cls) -> type[BaseModel]:
        return cls.target.related_model

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
        abstract = True
