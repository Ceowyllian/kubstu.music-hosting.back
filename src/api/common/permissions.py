from rest_framework.permissions import BasePermission

from db.person.models import WithOwnerMixin

__all__ = [
    "IsOwner",
]


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj: WithOwnerMixin):
        return request.user == obj.owner.user
