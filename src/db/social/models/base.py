from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = [
    "make_target_field",
]


def make_target_field(path_to_model: str):
    """
    :param path_to_model: should be a dotted path to django model "app_label.ModelClass"
    """
    model_name = path_to_model.split(".")[-1]
    return models.ForeignKey(
        to=path_to_model,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        editable=False,
        verbose_name=_(model_name),
    )
