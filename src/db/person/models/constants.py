from django.utils.translation import gettext_lazy as _
from model_utils import Choices

PERSON_ROLE_CHOICES = Choices(
    (0, "Admin", _("Admin")),
    (1, "Moderator", _("Moderator")),
    (2, "Singer", _("Moderator")),
)
