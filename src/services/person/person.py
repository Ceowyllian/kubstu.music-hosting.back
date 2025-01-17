from djoser.signals import user_registered

from db.person.models import Person
from services.common import model_update

__all__ = [
    "create_person",
    "update_person",
]


def create_person(sender, user, request, **kwargs):
    person = Person(user=user)
    person.full_clean()
    person.save()


user_registered.connect(create_person)


def update_person(instance, **data):
    instance, _ = model_update(
        instance=instance,
        fields=["avatar", "summary", "public_email"],
        data=data,
    )
    return instance
