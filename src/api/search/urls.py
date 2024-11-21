from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.search.views import SearchAllView

router = DefaultRouter()
router.register(r"", SearchAllView, "search-all")

urlpatterns = [
    path(r"", include(router.urls)),
]
