from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.music.views import TrackViewSet

tracks_router = DefaultRouter()
tracks_router.register(r"tracks", TrackViewSet, "tracks")

urlpatterns = [
    path(r"", include(tracks_router.urls)),
]
