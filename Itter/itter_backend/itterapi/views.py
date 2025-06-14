from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from supabase import create_client
from .models import UserProfile, Post, Like, Follow, User
from .forms import UserProfileForm, PostForm
from .serializers import UserProfileSerializer, PostSerializer, LikeSerializer, FollowSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
import os, secrets
from django.middleware.csrf import get_token
from django.core.mail import send_mail
# from . import forms

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

# Create your views here.
def default_index(request):
    return JsonResponse({"message":"Hey site is working, maybe"})

def create_user_and_profile(request):

    """
    Handles the creation of a new user and associated user profile.

    This view accepts only POST requests with JSON-encoded data. It initializes
    a UserProfileForm with the provided data, validates it, and saves a new 
    user profile. If the form is valid, it returns a JSON response with a success 
    message. If the form is invalid, it returns a JSON response with error details.

    Parameters:
    request (HttpRequest): The HTTP request object containing JSON data.

    Returns:
    JsonResponse: A JSON response with a success message or error details.
    """

    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)

            # Initialize forms with JSON data
            user_form = UserProfileForm(data)

            # Validate forms
            if user_form.is_valid():
                # Save UserProfile object
                profile = user_form.save()
                user = profile.user
                user.is_active = False
                user.save()
                
                verification_token = secrets.token_urlsafe(32)
                verification_url = request.build_absolute_uri(
                    reverse('verify_email', args=[verification_token])
                )
                
                send_mail(
                    'Verify your email for Itter',
                    f'Click the following link to verify your email: {verification_url}',
                    'fromitter@gmail.com',
                    [user.email],
                    fail_silently=False,
                )
                
                profile.verification_token = verification_token
                profile.save()

                return JsonResponse({'message': 'User and profile created successfully!'}, status=201)

            # Handle form errors
            errors = {**user_form.errors}
            return JsonResponse({'errors': errors}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=401)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def verify_email(request, token):
    try:
        profile = get_object_or_404(UserProfile, verification_token=token)
        user = profile.user
        user.is_active = True
        profile.verification_token = ''  # Clear the token
        user.save()
        return redirect("https://codecooker1.github.io/Signin")
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'Invalid verification token'}, status=400)


@require_http_methods(['POST'])
def create_post(request):
    """
    Handles the creation of a new post.

    Accepts only POST requests with form-encoded data. If the form is valid, it saves
    a new Post object with the current user and returns a JSON response with a success
    message and the post ID. If the form is invalid, it returns a JSON response with an
    error message. For GET requests, it returns a JSON response indicating the invalid
    request method.

    Parameters:
    request (HttpRequest): The HTTP request object containing POST data.

    Returns:
    JsonResponse: A JSON response with a success message and post ID, or an error message.
    """

    if request.method == 'POST':
        data = json.loads(request.body)
        form = PostForm(data, user=request.user)
        if form.is_valid():
            post = form.save()
            post.save()
            return JsonResponse({'message': 'Post created successfully!', "post_id": post.post_id}, status=201)
        else:
            return JsonResponse({'message': 'Invalid JSON', "form": data}, status=401)
    if request.method == 'GET':
       return JsonResponse({'message': 'Invalid request method GET'}, status = 405)

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
                'email': request.user.email,
                'profile_image': request.user.userprofile.profile_image,
                'bio': request.user.userprofile.bio,
                'following': request.user.userprofile.following,
                'followers': request.user.userprofile.followers,
            }
        )
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )
    
def follow_user(request, username):
    try:
        user = User.objects.get(username=username)
        is_following = Follow.objects.filter(follower=request.user, followee=user).exists()
        
        if is_following:
            follow = Follow.objects.get(follower=request.user, followee=user).delete()
        else:
            follow = Follow.objects.create(follower=request.user, followee=user)
            follow.save()
        return JsonResponse({'message': 'Followed successfully'})
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)
    
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(user = user).values()
        is_following = Follow.objects.filter(follower=request.user, followee=user).exists()
        return JsonResponse({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'profile_image': user.userprofile.profile_image,
            'bio': user.userprofile.bio,
            'following': user.userprofile.following,
            'followers': user.userprofile.followers,
            'is_following': is_following,
            'posts': list(posts),
        })
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)
    
from django.forms.models import model_to_dict

def get_feed(request):
    posts = Post.objects.all().order_by('-created_at')
    post_data = []
    for post in posts:
        post_dict = {
            'post_id': post.post_id,
        }
        post_data.append(post_dict)
    return JsonResponse({'posts': post_data})

def get_user_posts(request, username):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(user=user).order_by('-created_at')
        post_data = []
        for post in posts:
            post_dict = {
                'post_id': post.post_id,
                'user_id': post.user_id,
                'content': post.content,
                'image': post.media_url,
                'likes': post.likes.all().count(),
                "is_liked": post.is_liked(request.user),
                'created_at': post.created_at,
                # 'updated_at': post.updated_at,
            }
            post_data.append(post_dict)
        return JsonResponse({'posts': post_data})
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)
    
def get_post_details(request, pk):
    try:
        post = Post.objects.get(post_id=pk)
        return JsonResponse({
            'post_id': post.post_id,
            'user_id': post.user_id,
            'content': post.content,
            'image': post.media_url,
            'likes': post.likes.all().count(),
            "is_liked": post.is_liked(request.user),
            'created_at': post.created_at,
            # 'updated_at': post.updated_at,
            'user': {
                'username': post.user.username,
                'first_name': post.user.first_name,
                'last_name': post.user.last_name,
                'profile_image': post.user.userprofile.profile_image,
                'bio': post.user.userprofile.bio
            }
        })
    except Post.DoesNotExist:
        return JsonResponse({'message': 'Post not found'})
    
def update_like(request):
    data = json.loads(request.body)
    post = Post.objects.get(post_id=data["post_id"])
    
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            like = Like.objects.get(post=post, user=request.user)
            like.delete()
        except Like.DoesNotExist:
            like = Like.objects.create(post=post, user=request.user)
            like.save()
        return JsonResponse({'message': 'Like updated successfully!', 'isLikedAlready': post.is_liked(request.user)})
    if request.method == 'GET':
        return JsonResponse({'isLikedAlready': post.is_liked(request.user), 'likes': post.likes.all().count()})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    basename = 'user' # Important for reverse lookups
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    basename = 'post' # Important for reverse lookups
    permission_classes = [AllowAny]
    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()

    serializer_class = UserProfileSerializer
    
class PostDetailsView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    


def test_mail(request):
    try:
        send_mail('Subject here', 'Here is the message.', 'from@example.com', ['codecookermintz@proton.me'], fail_silently=False)
        return JsonResponse({'message': 'Email sent successfully'})
    except:
        return JsonResponse({'message': 'Email failed to send'})