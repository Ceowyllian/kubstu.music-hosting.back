from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = [
    "WithOwnerMixin",
]


class WithOwnerMixin(models.Model):

    owner = models.ForeignKey(
        "social.Person",
        on_delete=models.RESTRICT,
        blank=False,
        null=False,
        editable=False,
        verbose_name=_("Owner"),
    )

    class Meta:
        abstract = True
