from django.utils.translation import gettext_lazy as _

from api.common import (
    SCHEMA_TAG_MUSIC,
    DjangoFilterBackend,
    IsAuthenticatedOrReadOnly,
    IsOwner,
    ModelViewSet,
    OrderingFilter,
    Response,
    SearchFilter,
    action,
    extend_schema,
    extend_schema_view,
    status,
)
from api.music.filters import PlaylistFilterSet
from api.music.serializers import (
    PlaylistCreateSerializer,
    PlaylistSerializer,
    PlaylistUpdateSerializer,
    PlaylistWithTracksSerializer,
)
from db.music.models import Playlist
from services.music import (
    playlist_create,
    playlist_destroy,
    playlist_restore,
    playlist_update,
)

__all__ = [
    "PlaylistViewSet",
]


@extend_schema_view(
    list=extend_schema(
        summary=_("List of playlists"),
        responses={200: PlaylistSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary=_("Playlist"),
        responses={200: PlaylistWithTracksSerializer},
    ),
    create=extend_schema(
        summary=_("Create playlist"),
        request=PlaylistCreateSerializer,
        responses={201: PlaylistWithTracksSerializer},
    ),
    partial_update=extend_schema(
        summary=_("Update playlist"),
        request=PlaylistUpdateSerializer(partial=True),
        responses={200: PlaylistWithTracksSerializer},
    ),
    destroy=extend_schema(
        summary=_("Delete playlist"),
        responses={204: None},
    ),
)
@extend_schema(tags=[SCHEMA_TAG_MUSIC])
class PlaylistViewSet(
    ModelViewSet,
):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwner,
    ]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = PlaylistFilterSet
    search_fields = [
        "name",
        "owner__user__username",
    ]
    ordering_fields = [
        "name",
        "created",
        "modified",
    ]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PlaylistWithTracksSerializer
        if self.action == "list":
            return PlaylistSerializer

    def get_queryset(self):
        # TODO use selector instead
        return Playlist.available_objects.all()

    def create(self, request, *args, **kwargs):
        input_ = PlaylistCreateSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        playlist = playlist_create(user=request.user, **input_.validated_data)

        output = PlaylistSerializer(instance=playlist)
        return Response(output.data, status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        input_ = PlaylistUpdateSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        playlist = playlist_update(playlist=self.get_object(), **input_.validated_data)

        output = PlaylistSerializer(instance=playlist)
        return Response(output.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        playlist_destroy(self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses={200: PlaylistSerializer})
    @action(methods=["POST"], detail=True, permission_classes=[IsOwner])
    def restore(self, request, *args, **kwargs):
        playlist = playlist_restore(self.kwargs["pk"])
        output = PlaylistSerializer(instance=playlist)
        return Response(output.data, status.HTTP_200_OK)
