from django.utils.translation import gettext_lazy as _

from api.common import (
    SCHEMA_TAG_LIKES,
    CreateModelMixin,
    DestroyModelMixin,
    IsAuthenticated,
    Response,
    extend_schema,
    extend_schema_view,
    status,
)
from api.likes.serializers import LikeCreateOutputSerializer
from api.social import SocialTargetNestedView
from services.social import like_create, like_destroy

__all__ = [
    "LikeView",
]


@extend_schema_view(
    create=extend_schema(
        summary=_("Like the specified object"),
        responses={201: LikeCreateOutputSerializer},
    ),
    destroy=extend_schema(
        summary=_("Remove like from the specified object"),
        responses={204: None},
    ),
)
@extend_schema(tags=[SCHEMA_TAG_LIKES])
class LikeView(
    SocialTargetNestedView,
    CreateModelMixin,
    DestroyModelMixin,
):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        like = like_create(
            liked_by=request.user.person,
            target=self.get_target(),
        )
        output = LikeCreateOutputSerializer(like)
        return Response(output.data, status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        like_destroy(liked_by=request.user.person, target_id=self.target_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
