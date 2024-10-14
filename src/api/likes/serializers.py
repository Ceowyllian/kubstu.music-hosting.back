from api.common import DataObjectSerializer, fields
from db.social.models import Like
from db.social.models.constants import LIKE_TARGET_TYPE_CHOICES

__all__ = [
    "LikeCreateOutputSerializer",
]


class LikeCreateOutputSerializer(DataObjectSerializer):
    target_type = fields.ChoiceField(
        choices=LIKE_TARGET_TYPE_CHOICES,
    )

    class Meta(DataObjectSerializer.Meta):
        model = Like
        fields = DataObjectSerializer.Meta.fields + [
            "target_id",
            "owner_id",
            "target_type",
        ]
