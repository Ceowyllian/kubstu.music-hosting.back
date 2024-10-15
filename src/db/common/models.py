import uuid

from django.contrib.auth import get_user_model
from model_utils.fields import UUIDField
from model_utils.models import TimeStampedModel

__all__ = [
    "BaseModel",
]

User = get_user_model()


class BaseModel(
    TimeStampedModel,
):
    id = UUIDField(default=uuid.uuid4)

    class Meta:
        abstract = True
