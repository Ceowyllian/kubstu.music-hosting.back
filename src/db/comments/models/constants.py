from django.utils.translation import gettext_lazy as _
from model_utils import Choices

__all__ = [
    "COMMENT_STATUS_CHOICES",
]


COMMENT_STATUS_CHOICES = Choices(
    (0, "Visible", _("Visible")),
    (1, "Removed", _("Removed")),
)
