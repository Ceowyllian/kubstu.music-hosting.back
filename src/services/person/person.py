from djoser.signals import user_registered

from db.person.models import Person


def create_person(sender, user, request):
    person = Person(user=user)
    person.full_clean()
    person.save()


user_registered.connect(create_person)
