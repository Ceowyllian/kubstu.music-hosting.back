from api.common import DataObjectSerializer, fields
from db.person.models import Person

__all__ = [
    "MeSerializer",
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
