from django.middleware.common import MiddlewareMixin


class ExtractTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        token = request.COOKIES.get("auth_token", None)
        if token:
            request.META["HTTP_AUTHORIZATION"] = f"Token {token}"
