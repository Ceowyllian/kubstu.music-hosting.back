from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from db.common import BaseModel

__all__ = [
    "ReadOnlyMixin",
    "DataObjectSerializer",
]


class ReadOnlyMixin:
    def save(self, **kwargs):
        raise NotImplementedError(self.error_message)  # pragma: no cover

    def create(self, validated_data):
        raise NotImplementedError(self.error_message)  # pragma: no cover

    def update(self, instance, validated_data):
        raise NotImplementedError(self.error_message)  # pragma: no cover

    @property
    def error_message(self):
        return "`%s` serializer is supposed to be read-only." % self.__class__.__name__


class DataObjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        read_only=True,
        help_text=_("Object ID"),
    )
    created = serializers.DateTimeField(
        read_only=True,
        help_text=_("Creation date and time"),
    )
    modified = serializers.DateTimeField(
        read_only=True,
        help_text=_("Modification date and time"),
    )

    class Meta:
        model = BaseModel
        abstract = True
        fields = [
            "id",
            "created",
            "modified",
        ]
