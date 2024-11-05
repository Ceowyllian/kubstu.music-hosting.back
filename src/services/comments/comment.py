from django.contrib.contenttypes.models import ContentType

from db.comments.models import Comment, WithCommentsMixin
from db.comments.models.constants import COMMENT_STATUS_CHOICES
from services.common import model_update

__all__ = [
    "CommentModelService",
    "CommentInstanceService",
]


class CommentModelService:

    def __init__(self, target: WithCommentsMixin):
        self.target = target

    @property
    def comments_qs(self):
        return self.target.comments.all()

    def comment_create(
        self,
        *,
        user,
        subject: str,
        parent_id=None,
    ):
        ct = ContentType.objects.get_for_model(type(self.target))
        comment = Comment(
            target_id=self.target.id,
            owner=user.person,
            subject=subject,
            parent_id=parent_id,
            content_type=ct,
        )
        comment.full_clean()
        comment.save()
        return comment


class CommentInstanceService:

    def __init__(self, comment):
        self.comment = comment

    def comment_update(self, **data):
        model_update(instance=self.comment, fields=["subject"], **data)
        return self.comment

    def comment_destroy(self):
        self.comment_set_status(COMMENT_STATUS_CHOICES.Removed)

    def comment_restore(self):
        self.comment_set_status(COMMENT_STATUS_CHOICES.Visible)

    def comment_set_status(self, status):
        self.comment.status = status
        self.comment.full_clean()
        self.comment.save(update_fields=["status"])
