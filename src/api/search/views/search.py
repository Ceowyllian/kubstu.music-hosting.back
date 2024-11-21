from django.utils.translation import gettext_lazy as _

from api.common import (
    SCHEMA_TAG_SEARCH,
    AllowAny,
    GenericViewSet,
    ListModelMixin,
    Response,
    SearchFilter,
    extend_schema,
    extend_schema_view,
    status,
)
from api.search.filters import (
    AlbumSearchFilter,
    PersonSearchFilter,
    PlaylistSearchFilter,
    TrackSearchFilter,
)
from api.search.serializers import SearchSerializer, serialize_search_querysets
from db.music.models import Album, Playlist, Track
from db.person.models import Person

__all__ = [
    "SearchAllView",
]


@extend_schema_view(
    list=extend_schema(
        summary=_(""),
        responses=SearchSerializer(many=False),
    ),
)
@extend_schema(tags=[SCHEMA_TAG_SEARCH])
class SearchAllView(
    GenericViewSet,
    ListModelMixin,
):
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]

    def get_queryset(self):
        return {
            Track: TrackSearchFilter,
            Album: AlbumSearchFilter,
            Playlist: PlaylistSearchFilter,
            Person: PersonSearchFilter,
        }

    def filter_queryset(self, queryset):
        return [
            filter_().filter_queryset(self.request, model.objects.all(), self)
            for model, filter_ in self.get_queryset().items()
        ]

    def list(self, request, *args, **kwargs):
        querysets = self.filter_queryset(self.get_queryset())
        pages = [self.paginate_queryset(qs) for qs in querysets]
        data = serialize_search_querysets(*pages)
        return Response(data, status.HTTP_200_OK)
