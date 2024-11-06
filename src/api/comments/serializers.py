from api.common import DataObjectSerializer, EmptySerializer, fields

__all__ = [
    "NestedCommentListSerializer",
    "CommentCreateSerializer",
    "CommentRetrieveSerializer",
    "CommentUpdateSerializer",
]

from db.comments.models import Comment


class NestedCommentListSerializer(DataObjectSerializer):
    class Meta(DataObjectSerializer.Meta):
        model = Comment
        fields = DataObjectSerializer.Meta.fields + [
            "subject",
            "parent_id",
            "status",
        ]


class CommentCreateSerializer(EmptySerializer):
    subject = fields.CharField()
    parent_id = fields.UUIDField(
        default=None,
    )


class CommentRetrieveSerializer(DataObjectSerializer):
    class Meta(DataObjectSerializer.Meta):
        model = Comment
        fields = DataObjectSerializer.Meta.fields + [
            "subject",
            "parent_id",
            "status",
        ]


class CommentUpdateSerializer(EmptySerializer):
    subject = fields.CharField()
