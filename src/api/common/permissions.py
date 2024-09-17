from rest_framework.permissions import (
    AllowAny,
    BasePermission,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from db.person.models import WithOwnerMixin

__all__ = [
    "AllowAny",
    "IsAuthenticated",
    "IsAuthenticatedOrReadOnly",
    "IsOwner",
    "BasePermission",
]


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj: WithOwnerMixin):
        return request.user == obj.owner.user
