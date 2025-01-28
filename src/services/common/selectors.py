from django.db.models import QuerySet

from db.person.models import WithOwnerMixin

__all__ = [
    "select_related_owner",
]


def select_related_owner(qs: QuerySet[WithOwnerMixin]):
    return qs.select_related("owner", "owner__user")
