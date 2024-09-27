from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common import BaseModel
from db.person.models import WithOwnerMixin

__all__ = [
    "make_target_field",
    "CommentBase",
    "RepostBase",
    "LikeBase",
]


def make_target_field(path_to_model: str):
    """
    :param path_to_model: should be a dotted path to django model "app_label.ModelClass"
    """
    model_name = path_to_model.split(".")[-1]
    return models.ForeignKey(
        to=path_to_model,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_(model_name),
    )


class SocialModel(BaseModel, WithOwnerMixin):
    target: type[models.Model] = None

    def __str__(self):
        return f"{self.owner.username} - {self.target}"

    class Meta:
        abstract = True


class CommentBase(SocialModel):
    subject = models.TextField(
        blank=False,
        null=False,
        editable=True,
        verbose_name=_("Subject"),
    )

    def __str__(self):
        return f"{self.owner.username} - {self.subject}"

    class Meta(SocialModel.Meta):
        abstract = True


class RepostBase(SocialModel):

    class Meta(SocialModel.Meta):
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=("owner", "target"), name="unique_%(class)s"
            ),
        ]


class LikeBase(SocialModel):

    class Meta(SocialModel.Meta):
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=("owner", "target"), name="unique_%(class)s"
            ),
        ]
