from django.urls import include, path

urlpatterns = [
    path(r"auth/", include("api.auth.urls")),
    path(r"music/", include("api.music.urls")),
    path(r"my/", include("api.my.urls")),
    path(r"me/", include("api.me.urls")),
    path(r"search/", include("api.search.urls")),
    # the path is not specified intentionally
    path(r"", include("api.likes.urls")),
    path(r"", include("api.comments.urls")),
]
