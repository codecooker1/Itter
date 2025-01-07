from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from supabase import create_client
from .models import UserProfile, Post, Like, Follow, User
from .forms import UserProfileForm
from .serializers import UserProfileSerializer, PostSerializer, LikeSerializer, FollowSerializer
from rest_framework import viewsets
import os
# from . import forms

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()

    serializer_class = UserProfileSerializer

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
def create_user_and_profile(request):
    """
    Creates a new user and profile from JSON data in the request body.

    Example of request body:
    {
        "username": "johnDoe",
        "email": "john@example.com",
        "password": "mySecretPassword",
        "bio": "I am a software engineer.",
        "profile_image": "https://example.com/johndoe.jpg"
    }

    Returns a JSON response with a success message and HTTP status 201 if the user and profile are created successfully.
    Returns a JSON response with form errors and HTTP status 400 if the request body contains invalid data.
    Returns a JSON response with an error message and HTTP status 400 if the request body is not valid JSON.
    Returns a JSON response with an error message and HTTP status 405 if the request method is not POST.
    """
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)

            # Initialize forms with JSON data
            user_form = UserProfileForm({
                'firstname': data.get('firstname'),
                'lastname': data.get('lastname'),
                'username': data.get('username'),
                'email': data.get('email'),
                'password': data.get('password'),
                'bio': data.get('bio'),
                'profile_image': data.get('profile_image'),
            })

            # Validate forms
            if user_form.is_valid():
                # Save UserProfile object
                profile = user_form.save()
                profile.save()

                return JsonResponse({'message': 'User and profile created successfully!'}, status=201)

            # Handle form errors
            errors = {**user_form.errors}
            return JsonResponse({'errors': errors}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=401)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        # data = json.loads(request.body.decode('utf-8'))
        return JsonResponse({'message': str(request.body)})
    if request.method == 'GET':
       return JsonResponse({'message': 'Invalid request method GET'})

@require_http_methods(['POST'])
@csrf_exempt
def login_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        password = data['password']
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON'}, status=400
        )

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse(
            {'success': False, 'message': 'Invalid email'}, status=401
        )

    user = authenticate(request, username=user.username, password=password)

    if user:
        login(request, user)
        print('login successful')
        return JsonResponse({'success': True})
    else:
        print('login failed')
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
            {
                'username': request.user.username,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'profile_image': request.user.userprofile.profile_image,
                'bio': request.user.userprofile.bio
            }
        )
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )

def getNameHandle(request, user_id):

    try:
        user = User.objects.get(pk=user_id)
        user_profile = UserProfile.objects.get(user=user)

        data = {
            'first_name': user_profile.user.first_name,
            'last_name': user_profile.user.last_name,
            'username': user_profile.user.username,
        }

        return JsonResponse(data, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    basename = 'user' # Important for reverse lookups

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    basename = 'post' # Important for reverse lookups