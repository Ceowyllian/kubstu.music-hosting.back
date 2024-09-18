from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.mixins import UpdateModelMixin as DrfUpdateModelMixin
from rest_framework.views import APIView, View
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet as DrfModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSetMixin

__all__ = [
    "ListModelMixin",
    "RetrieveModelMixin",
    "CreateModelMixin",
    "UpdateModelMixin",
    "DestroyModelMixin",
    "GenericViewSet",
    "ModelViewSet",
    "ReadOnlyModelViewSet",
    "ViewSetMixin",
    "View",
    "APIView",
]


class UpdateModelMixin(DrfUpdateModelMixin):
    http_method_names = ["get", "post", "patch", "delete"]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ModelViewSet(
    DrfModelViewSet,
    UpdateModelMixin,
):
    pass
