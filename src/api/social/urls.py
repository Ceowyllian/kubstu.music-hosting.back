from django.urls import include, path
from rest_framework.routers import DefaultRouter

__all__ = [
    "like_url",
    "comments_url",
]


def social_url(prefix, view_class, basename, social_type):
    router = DefaultRouter()
    router.register(social_type, view_class, f"{basename}-{social_type}")
    return path(rf"{prefix}/<uuid:target_pk>/", include(router.urls))


def like_url(prefix, view_class, basename):
    return social_url(prefix, view_class, basename, "like")


def comments_url(prefix, view_class, basename):
    return social_url(prefix, view_class, basename, "comments")
