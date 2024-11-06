from api.comments.serializers import CommentRetrieveSerializer, CommentUpdateSerializer
from api.common import (
    SCHEMA_TAG_COMMENTS,
    DestroyModelMixin,
    GenericViewSet,
    IsOwner,
    Response,
    UpdateModelMixin,
    extend_schema,
    extend_schema_view,
    status,
)
from db.comments.models import Comment
from services.comments import CommentInstanceService

__all__ = [
    "CommentsView",
]


@extend_schema_view(
    partial_update=extend_schema(
        request=CommentUpdateSerializer,
        responses={200: CommentUpdateSerializer},
    ),
    destroy=extend_schema(responses={204: None}),
)
@extend_schema(tags=[SCHEMA_TAG_COMMENTS])
class CommentsView(
    GenericViewSet,
    UpdateModelMixin,
    DestroyModelMixin,
):
    permission_classes = [IsOwner]
    queryset = Comment.objects.all()

    def update(self, request, *args, **kwargs):
        service = CommentInstanceService(self.get_object())
        input_ = CommentUpdateSerializer(data=request.data, partial=True)
        input_.is_valid(raise_exception=True)
        instance = service.comment_update(**input_.validated_data)
        output = CommentRetrieveSerializer(instance)
        return Response(output.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        service = CommentInstanceService(self.get_object())
        service.comment_destroy()
        return Response(status=status.HTTP_204_NO_CONTENT)
