from django.db import models
from django.utils.translation import gettext_lazy as _

from db.common.models import BaseModel
from db.person.models.constants import PERSON_ROLE_CHOICES

__all__ = [
    "PersonRole",
]


class PersonRole(BaseModel):
    person = models.ForeignKey(
        "person.Person",
        on_delete=models.RESTRICT,
        verbose_name=_("Person"),
    )
    role = models.PositiveIntegerField(
        null=False,
        blank=False,
        editable=False,
        choices=PERSON_ROLE_CHOICES,
        verbose_name=_("Role identifier"),
    )

    class Meta(BaseModel.Meta):
        constraints = [
            models.UniqueConstraint(fields=("person", "role"), name="unique_%(class)s"),
        ]
        verbose_name = _("Person role")
        verbose_name_plural = _("Person roles")
