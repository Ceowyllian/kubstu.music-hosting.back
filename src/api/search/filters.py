from api.common import SearchFilter

__all__ = [
    "TrackSearchFilter",
    "AlbumSearchFilter",
    "PlaylistSearchFilter",
    "PersonSearchFilter",
]


class TrackSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        return ["title", "description"]


class AlbumSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        return ["title"]


class PlaylistSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        return ["title"]


class PersonSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        return ["user__username"]
