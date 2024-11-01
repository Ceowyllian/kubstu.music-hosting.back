from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

__all__ = [
    "WithLikesMixin",
]


class WithLikesMixin(models.Model):
    likes = GenericRelation(
        "likes.Like",
        "target_id",
        "content_type",
    )

    class Meta:
        abstract = True
