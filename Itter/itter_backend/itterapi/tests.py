import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import User, UserProfile, Post, Like, Follow
from .forms import PostForm, UserProfileForm

class UserTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_user_profile_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        profile = UserProfile.objects.create(user=user)
        self.assertEqual(profile.user, user)

class PostTests(TestCase):
    def test_post_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        post = Post.objects.create(user=user, content='Test post')
        self.assertEqual(post.user, user)
        self.assertEqual(post.content, 'Test post')

    def test_post_likes(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        post = Post.objects.create(user=user, content='Test post')
        like = Like.objects.create(user=user, post=post)
        self.assertEqual(post.likes, 1)

class LikeTests(TestCase):
    def test_like_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        post = Post.objects.create(user=user, content='Test post')
        like = Like.objects.create(user=user, post=post)
        self.assertEqual(like.user, user)
        self.assertEqual(like.post, post)

class FollowTests(TestCase):
    def test_follow_creation(self):
        user1 = User.objects.create_user(username='testuser1', email='test1@example.com', password='password')
        user2 = User.objects.create_user(username='testuser2', email='test2@example.com', password='password')
        follow = Follow.objects.create(follower=user1, followee=user2)
        self.assertEqual(follow.follower, user1)
        self.assertEqual(follow.followee, user2)

class PostFormTests(TestCase):
    def test_valid_form(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        form = PostForm({'content': 'Test post'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())

class UserProfileFormTests(TestCase):
    def test_valid_form(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        form = UserProfileForm({'bio': 'Test bio', 'profile_image': 'test_image.jpg'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = UserProfileForm({'bio': '', 'profile_image': ''})
        self.assertFalse(form.is_valid())

class ViewTests(TestCase):
    def test_default_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Hey site is working, maybe')

    def test_create_post(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client.force_login(user)
        response = self.client.post(reverse('create_post'), {'content': 'Test post'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Post created successfully!')

    def test_set_csrf_token(self):
        response = self.client.get(reverse('set_csrf_token'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'CSRF cookie set')

    def test_logout_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client.force_login(user)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Logged out')

    def test_login_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Logged in')

    def test_user_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client.force_login(user)
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], 'testuser')

    def test_user_profile_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        profile = UserProfile.objects.create(user=user)
        self.client.force_login(user)
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['bio'], '')

    def test_post_list_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        post1 = Post.objects.create(user=user, content='Test post 1')
        post2 = Post.objects.create(user=user, content='Test post 2')
        self.client.force_login(user)
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_post_detail_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        post = Post.objects.create(user=user, content='Test post')
        self.client.force_login(user)
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['content'], 'Test post')

    def test_like_list_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        post = Post.objects.create(user=user, content='Test post')
        like1 = Like.objects.create(user=user, post=post)
        like2 = Like.objects.create(user=user, post=post)
        self.client.force_login(user)
        response = self.client.get(reverse('like_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_follow_list_view(self):
        user1 = User.objects.create_user(username='testuser1', email='test1@example.com', password='password')
        user2 = User.objects.create_user(username='testuser2', email='test2@example.com', password='password')
        follow1 = Follow.objects.create(follower=user1, followee=user2)
        follow2 = Follow.objects.create(follower=user1, followee=user2)
        self.client.force_login(user1)
        response = self.client.get(reverse('follow_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)