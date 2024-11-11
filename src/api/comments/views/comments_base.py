from django.utils.translation import gettext_lazy as _

from api.comments.serializers import (
    CommentCreateSerializer,
    CommentRetrieveSerializer,
    NestedCommentListSerializer,
)
from api.common import (
    SCHEMA_TAG_COMMENTS,
    CreateModelMixin,
    IsAuthenticatedOrReadOnly,
    ListModelMixin,
    Response,
    extend_schema,
    extend_schema_view,
    status,
)
from api.social import SocialTargetNestedView
from services.comments import CommentModelService

__all__ = [
    "CommentsNestedView",
]


@extend_schema_view(
    list=extend_schema(
        summary=_("Сomments associated with this object"),
        responses={200: NestedCommentListSerializer(many=True)},
    ),
    create=extend_schema(
        summary=_("Add a comment to a given object"),
        responses={201: CommentRetrieveSerializer},
    ),
)
@extend_schema(tags=[SCHEMA_TAG_COMMENTS])
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
