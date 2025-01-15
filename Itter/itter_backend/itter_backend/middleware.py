from http import cookies
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponseBase
from django.middleware.common import CommonMiddleware
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
                
        response["Access-Control-Allow-Origin"] = "https://codecooker1.github.io"

        return response
    

class AllowCorsMiddleware(CommonMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'https://codecooker1.github.io'
        response['Access-Control-Allow-Credentials'] = 'true'
        return super().process_response(request, response)