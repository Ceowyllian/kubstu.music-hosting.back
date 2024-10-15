from django.utils.translation import gettext_lazy as _

from api.common import (
    SCHEMA_TAG_MUSIC,
    AllowAny,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
    IsOwner,
    ListModelMixin,
    Response,
    extend_schema,
    extend_schema_view,
    status,
)
from api.music.serializers import PlaylistAddTrackSerializer, TrackRetrieveSerializer
from db.music.models import Track
from services.music import playlist_add_track, playlist_remove_track

__all__ = [
    "PlaylistTracksViewSet",
]


@extend_schema_view(
    create=extend_schema(
        summary=_("Add a track to the playlist"),
        request=PlaylistAddTrackSerializer,
        responses={201: TrackRetrieveSerializer},
    ),
    list=extend_schema(
        summary=_("List of tracks of the playlists"),
        responses={200: TrackRetrieveSerializer(many=True)},
    ),
    destroy=extend_schema(
        summary=_("Remove the track from the playlist"),
        responses={204: None},
    ),
)
@extend_schema(tags=[SCHEMA_TAG_MUSIC])
class PlaylistTracksViewSet(
    GenericViewSet,
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):

    def get_permissions(self):
        if self.action in ("create", "destroy"):
            return [IsOwner()]
        if self.action == "list":
            return [AllowAny()]

    def get_serializer_class(self):
        if self.action == "list":
            return TrackRetrieveSerializer

    def get_queryset(self):
        # TODO use selector instead
        return Track.objects.filter(
            playlisttrack__playlist__id=self.kwargs["playlist_pk"]
        )

    def create(self, request, *args, **kwargs):
        input_ = PlaylistAddTrackSerializer(data=request.data)
        input_.is_valid(raise_exception=True)

        track = playlist_add_track(
            playlist_id=self.kwargs["playlist_pk"],
            track_id=self.kwargs["pk"],
        )

        output = TrackRetrieveSerializer(instance=track)

        return Response(output.data, status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        playlist_remove_track(
            playlist_id=self.kwargs["playlist_pk"],
            track_id=self.kwargs["pk"],
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
