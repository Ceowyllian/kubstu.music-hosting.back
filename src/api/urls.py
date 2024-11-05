from django.urls import include, path

urlpatterns = [
    path(r"auth/", include("api.auth.urls")),
    path(r"music/", include("api.music.urls")),
    # the path is not specified intentionally
    path(r"", include("api.likes.urls")),
    path(r"", include("api.comments.urls")),
]
