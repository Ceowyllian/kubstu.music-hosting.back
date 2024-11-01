from api.common import (
    SCHEMA_TAG_LIKES,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
    IsAuthenticated,
    Response,
    extend_schema,
    status,
)
from api.likes.serializers import LikeCreateOutputSerializer
from services.social import like_create, like_destroy

__all__ = [
    "LikeView",
]


@extend_schema(tags=[SCHEMA_TAG_LIKES])
class LikeView(
    GenericViewSet,
    CreateModelMixin,
    DestroyModelMixin,
):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses={201: LikeCreateOutputSerializer})
    def create(self, request, *args, **kwargs):
        like = like_create(
            liked_by=request.user.person,
            target=self.get_object(),
        )
        output = LikeCreateOutputSerializer(like)
        return Response(output.data, status.HTTP_201_CREATED)

    @extend_schema(responses={204: None})
    def destroy(self, request, *args, **kwargs):
        like_destroy(liked_by=request.user.person, target_id=self.target_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
