from django.urls import path

from api.stream_audio.views import stream_view

urlpatterns = [
    path(r"<str:filename>/", stream_view),
]
