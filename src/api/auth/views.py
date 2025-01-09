from datetime import timedelta

from djoser.views import TokenCreateView, TokenDestroyView


class CustomTokenCreateView(TokenCreateView):

    def _action(self, serializer):
        response = super()._action(serializer)
        response.set_cookie(
            key="auth_token",
            value=response.data["auth_token"],
            max_age=timedelta(days=15),
            secure=True,
            httponly=True,
            samesite="Strict",
        )
        return response


class CustomTokenDestroyView(TokenDestroyView):
    def post(self, request):
        response = super().post(request)
        response.delete_cookie("auth_token")
        return response
