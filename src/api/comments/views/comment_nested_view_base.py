from api.comments.serializers import (
    CommentCreateSerializer,
    CommentRetrieveSerializer,
    NestedCommentListSerializer,
)
from api.common import (
    CreateModelMixin,
    GenericViewSet,
    IsAuthenticatedOrReadOnly,
    ListModelMixin,
    Response,
    get_object_or_404,
    status,
)
from services.comments import CommentModelService

__all__ = [
    "CommentsNestedView",
]


class CommentsNestedView(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
):
    target_model_class = NotImplemented
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    @property
    def target(self):
        return get_object_or_404(self.target_model_class, pk=self.kwargs["target_pk"])

    @property
    def service(self):
        return CommentModelService(self.target)

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
