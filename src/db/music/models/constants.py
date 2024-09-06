from django.utils.translation import gettext_lazy as _
from model_utils import Choices

__all__ = [
    "GENRE_CHOICES",
]


GENRE_CHOICES = Choices(
    (0, "ROCK", _("Rock")),
)
