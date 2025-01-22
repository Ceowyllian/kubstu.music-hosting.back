from api.common import DataObjectSerializer, EmptySerializer, fields
from db.person.models import Person

__all__ = [
    "MeSerializer",
    "PersonUpdateSerializer",
]


class MeSerializer(DataObjectSerializer):
    username = fields.CharField(
        source="user.username",
    )

    class Meta(DataObjectSerializer.Meta):
        model = Person
        fields = DataObjectSerializer.Meta.fields + [
            "user_id",
            "username",
            "avatar",
            "summary",
            "public_email",
        ]


class PersonUpdateSerializer(EmptySerializer):
    avatar = fields.ImageField(
        allow_null=True,
    )
    summary = fields.CharField(
        allow_null=True,
    )
    public_email = fields.CharField(
        allow_null=True,
        allow_blank=True,
    )
