from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from .models import User, Post


@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({'message': 'CSRF cookie set'})

# Create your views here.
def default_index(request):
    return JsonResponse({"message":"Hey site is working, maybe"})

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        # data = json.loads(request.body.decode('utf-8'))
        return JsonResponse({'message': str(request.body)})
    if request.method == 'GET':
       return JsonResponse({'message': 'Invalid request method GET'})