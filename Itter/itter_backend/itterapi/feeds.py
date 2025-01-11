# Create a class for generating user post feed using django feeds framework
from django.contrib.syndication.views import Feed
from .models import Post

class PostFeed(Feed):
    title = "Post Feed"
    link = "/feed/"
    description = "Latest posts"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.content

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return f"/posts/{item.post_id}/"

    def item_author_name(self, item):
        return item.user.username

    def item_pubdate(self, item):
        return item.created_at