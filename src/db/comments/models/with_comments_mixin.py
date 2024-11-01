from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

__all__ = [
    "WithCommentsMixin",
]


class WithCommentsMixin(models.Model):
    comments = GenericRelation(
        "comments.Comment",
        "target_id",
        "content_type",
    )

    class Meta:
        abstract = True
