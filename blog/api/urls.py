from django.urls import path
from rest_framework.routers import SimpleRouter

from blog.api.views import CreatePostApiViews, DetailPostAPIView, ListPostAPIView, PostViewSet,CommentCreateUpdateViewSet
from blog.models import Post

blog_router = SimpleRouter()
blog_router.register("posts", PostViewSet, basename="post")
blog_router.register("comments", CommentCreateUpdateViewSet, basename="comments")


app_name = "blog"

# urlpatterns = [
#     path("", ListPostAPIView.as_view(), name="list_post"),
#     # path("create/", CreatePostApiViews.as_view(), name="create_post"),
#     # path("<str:slug>/", DetailPostAPIView.as_view(), name="detail_post"),
# ]
