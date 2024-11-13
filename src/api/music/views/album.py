from api.common import (
    SCHEMA_TAG_MUSIC,
    AllowAny,
    DjangoFilterBackend,
    GenericViewSet,
    IsAuthenticatedOrReadOnly,
    IsOwner,
    ListModelMixin,
    OrderingFilter,
    Response,
    SearchFilter,
    extend_schema,
    status,
)
from api.music.filters import AlbumFilterSet
from api.music.serializers import (
    AlbumCreateSerializer,
    AlbumSerializer,
    AlbumUpdateSerializer,
    AlbumWithTracksSerializer,
)
from api.music.views.track_collection_base import TrackCollectionViewSet
from db.music.models import Album
from services.music import album_create, album_destroy, album_update

__all__ = [
    "AlbumViewSet",
    "AlbumTrackViewSet",
    "AlbumListView",
]


class AlbumListView(
    GenericViewSet,
    ListModelMixin,
):
    permission_classes = [
        AllowAny,
    ]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = AlbumFilterSet
    search_fields = [
        "title",
        "descriptions",
    ]
    ordering_fields = [
        "title",
        "release_date",
        "created",
        "modified",
    ]


@extend_schema(tags=[SCHEMA_TAG_MUSIC])
class AlbumViewSet(AlbumListView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwner,
    ]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AlbumWithTracksSerializer
        if self.action == "list":
            return AlbumSerializer

    def get_queryset(self):
        # TODO use selector instead
        return Album.objects.all()

    def create(self, request, *args, **kwargs):
        input_ = AlbumCreateSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        album = album_create(user=request.user, **input_.validated_data)

        output = AlbumWithTracksSerializer(instance=album)
        return Response(output.data, status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        input_ = AlbumUpdateSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        album = album_update(self.get_object(), **input_.validated_data)

        output = AlbumSerializer(instance=album)
        return Response(output.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        album_destroy(self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumTrackViewSet(TrackCollectionViewSet):
    collection_model_class = Album
