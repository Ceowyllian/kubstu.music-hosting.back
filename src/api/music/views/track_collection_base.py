from api.common import (
    SCHEMA_TAG_MUSIC,
    AllowAny,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
    IsOwner,
    ListModelMixin,
    Response,
    action,
    extend_schema,
    get_object_or_404,
    status,
)
from api.music.serializers import (
    CollectionAddTrackSerializer,
    CollectionSwapTracksSerializer,
    TrackRetrieveSerializer,
)
from services.music import TrackCollectionService

__all__ = [
    "TrackCollectionViewSet",
]


@extend_schema(tags=[SCHEMA_TAG_MUSIC])
class TrackCollectionViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
):
    collection_model_class = NotImplemented

    @property
    def service(self):
        return TrackCollectionService(self.get_object())

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        if self.action in ("create", "destroy", "swap"):
            return [IsOwner()]

    def get_object(self):
        qs = self.collection_model_class.objects.all()
        obj = get_object_or_404(qs, pk=self.kwargs["parent_pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        if self.action == "list":
            return self.service.tracks_qs

    def create(self, request, *args, **kwargs):
        input_ = CollectionAddTrackSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        track = self.service.add_track(**input_.validated_data)

        output = TrackRetrieveSerializer(instance=track)

        return Response(output.data, status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        self.service.remove_track(kwargs["pk"])
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST"], detail=False)
    def swap(self, request, *args, **kwargs):
        input_ = CollectionSwapTracksSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        left, right = self.service.swap_tracks(**input_.validated_data)

        output = TrackRetrieveSerializer(instance=(left, right), many=True)
        return Response(output.data, status.HTTP_200_OK)
