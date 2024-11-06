from api.comments.serializers import (
    CommentCreateSerializer,
    CommentRetrieveSerializer,
    NestedCommentListSerializer,
)
from api.common import (
    CreateModelMixin,
    IsAuthenticatedOrReadOnly,
    ListModelMixin,
    Response,
    status,
)
from api.social import SocialTargetNestedView
from services.comments import CommentModelService

__all__ = [
    "CommentsNestedView",
]


class CommentsNestedView(
    SocialTargetNestedView,
    ListModelMixin,
    CreateModelMixin,
):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    @property
    def service(self):
        return CommentModelService(self.get_target())

    def get_queryset(self):
        return self.service.comments_qs

    def get_serializer_class(self):
        if self.action == "list":
            return NestedCommentListSerializer

    def create(self, request, *args, **kwargs):
        input_ = CommentCreateSerializer(data=request.data)
        input_.is_valid(raise_exception=True)
        comment = self.service.comment_create(
            user=self.request.user,
            **input_.validated_data,
        )
        output = CommentRetrieveSerializer(comment)
        return Response(output.data, status.HTTP_201_CREATED)
