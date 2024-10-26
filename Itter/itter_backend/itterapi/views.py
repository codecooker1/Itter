from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from supabase import create_client
from .models import User, Post
import os

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

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

@require_http_methods(['POST'])
def login_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        password = data['password']
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON'}, status=400
        )

    user = authenticate(request, username=email, password=password)

    if user:
        login(request, user)
        return JsonResponse({'success': True})
    return JsonResponse(
        {'success': False, 'message': 'Invalid credentials'}, status=401
    )
    
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})


@require_http_methods(['GET'])
def user(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {'username': request.user.username, 'email': request.user.email}
        )
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def register(request):
    data = json.loads(request.body.decode('utf-8'))
    form = CreateUserForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'User registered successfully'}, status=201)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'error': errors}, status=400)
    
def getSampleIcon(request):
    url = supabase.storage.from_('profilepics').get_public_url('1.jpeg')
    # ,
    # {
    #     'transform': {
    #     'width': 500,
    #     'height': 500,
    #     },
    # })
    
    return JsonResponse({'image_url': url})
