from django.apps import AppConfig


class PersonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "db.person"

    def ready(self):
        from services import person  # noqa
