from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from db.likes.models import Like

__all__ = [
    "like_create",
    "like_destroy",
]


def like_create(*, liked_by, target_id, target_type):
    like = Like(
        target_id=target_id,
        target_type=target_type,
        owner=liked_by,
    )
    like.full_clean()
    like.save()


def like_destroy(*, liked_by, target_id):
    try:
        Like.objects.get(target_id=target_id, owner=liked_by).delete()
    except Like.DoesNotExist as e:
        raise ValidationError(_("You have not liked this post yet.")) from e
