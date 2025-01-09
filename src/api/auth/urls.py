from django.urls import include, path, re_path

from api.auth.views import CustomTokenCreateView, CustomTokenDestroyView

urlpatterns = [
    path("", include("djoser.urls")),
    re_path(r"^token/login/?$", CustomTokenCreateView.as_view(), name="login"),
    re_path(r"^token/logout/?$", CustomTokenDestroyView.as_view(), name="logout"),
]
