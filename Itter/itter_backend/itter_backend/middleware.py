from http import cookies
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponseBase
from django.conf import settings

cookies.Morsel._flags.add("partitioned")
cookies.Morsel._reserved.setdefault("partitioned", "Partitioned")

class CookiePartitioningMiddleware(MiddlewareMixin):
    def process_response(
        self, request: HttpRequest, response: HttpResponseBase
    ) -> HttpResponseBase:
        for name in (
            getattr(settings, f"{prefix}_COOKIE_NAME")
            for prefix in ("CSRF", "SESSION", "LANGUAGE")
            if getattr(settings, f"{prefix}_COOKIE_SECURE")
        ):
            if cookie := response.cookies.get(name):
                cookie["Partitioned"] = True

        return response