from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from db.common import BaseModel
from db.person.models import Person

from . import fields

__all__ = [
    "ReadOnlyMixin",
    "ModelSerializer",
    "DataObjectSerializer",
    "EmptySerializer",
    "PersonSerializer",
]


class ReadOnlyMixin:
    def save(self, **kwargs):
        raise TypeError(self.error_message)  # pragma: no cover

    def create(self, validated_data):
        raise TypeError(self.error_message)  # pragma: no cover

    def update(self, instance, validated_data):
        raise TypeError(self.error_message)  # pragma: no cover

    @property
    def error_message(self):
        return "`%s` serializer is supposed to be read-only." % self.__class__.__name__


class ModelSerializer(
    serializers.ModelSerializer,
    ReadOnlyMixin,
):
    id = serializers.UUIDField(
        read_only=True,
        help_text=_("Object ID"),
    )

    class Meta:
        model = BaseModel
        abstract = True
        fields = [
            "id",
        ]


class DataObjectSerializer(ModelSerializer):
    created = serializers.DateTimeField(
        read_only=True,
        help_text=_("Creation date and time"),
    )
    modified = serializers.DateTimeField(
        read_only=True,
        help_text=_("Modification date and time"),
    )

    class Meta(ModelSerializer.Meta):
        abstract = True
        fields = ModelSerializer.Meta.fields + [
            "created",
            "modified",
        ]


class EmptySerializer(serializers.Serializer):
    pass


class PersonSerializer(DataObjectSerializer):
    username = fields.CharField(
        source="user.username",
    )

    class Meta(DataObjectSerializer.Meta):
        model = Person
        fields = DataObjectSerializer.Meta.fields + [
            "user_id",
            "username",
            "avatar",
        ]
