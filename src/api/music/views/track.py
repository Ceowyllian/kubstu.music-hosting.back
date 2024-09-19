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
    extend_schema,
    extend_schema_view,
    status,
)
from api.music.serializers import (
    TrackCreateSerializer,
    TrackListSerializer,
    TrackRetrieveSerializer,
    TrackUpdateSerializer,
)
from db.music.models import Track

__all__ = [
    "TrackViewSet",
]


@extend_schema_view(
    list=extend_schema(
        summary=_("List of tracks"),
        responses={200: TrackListSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary=_("Track"),
        responses={200: TrackListSerializer},
    ),
    create=extend_schema(
        summary=_("Create track"),
        request=TrackCreateSerializer,
        responses={201: TrackRetrieveSerializer},
    ),
    partial_update=extend_schema(
        summary=_("Update track"),
        request=TrackUpdateSerializer(partial=True),
        responses={200: TrackRetrieveSerializer},
    ),
    destroy=extend_schema(
        summary=_("Delete track"),
        responses={204: None},
    ),
)
@extend_schema(tags=[SCHEMA_TAG_MUSIC])
class TrackViewSet(
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
    filterset_fields = [
        "owner__id",
        "owner__user__username",
        "genre",
        "duration",
        "release_date",
        "created",
        "modified",
    ]
    search_fields = [
        "title",
        "description",
    ]
    ordering_fields = [
        "genre",
        "title",
        "duration",
        "release_date",
    ]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TrackRetrieveSerializer
        if self.action == "list":
            return TrackListSerializer

    def get_queryset(self):
        return Track.objects.all()

    def create(self, request, *args, **kwargs):
        input_ = TrackCreateSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        # TODO: call track_create service
        track = None

        output = TrackRetrieveSerializer(instance=track)
        return Response(output.data, status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        input_ = TrackUpdateSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        # TODO: call track_update service
        track = None

        output = TrackRetrieveSerializer(instance=track)
        return Response(output.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        # TODO: call track_destroy service
        return Response(status=status.HTTP_204_NO_CONTENT)