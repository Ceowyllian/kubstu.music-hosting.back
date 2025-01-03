from django.urls import path

from api.me.views import MeView

urlpatterns = [path(r"", MeView.as_view())]
