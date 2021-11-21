from blog.api.paginations import PostPagination
from blog.api.permissions import IsCommentUserReadOnly
from blog.api.serializers import (
    CommentCreateUpdateSerializer,
    PostDetailSerializer,
    PostSerializer,
    PostUpdateCreateSerializer,
)
from blog.models import Comment, Post
from django.contrib.auth.decorators import login_required
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializer
    pagination_class = PostPagination
    lookup_field = "slug"
    search_fields = ("title", "description")

    def get_serializer_class(self):
        if self.action == "update":
            return PostUpdateCreateSerializer
        if self.action == "retrieve":
            return PostDetailSerializer
        return super().get_serializer_class()


class CreatePostApiViews(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostUpdateCreateSerializer
    # postu yazana custom permission eklenecek
    # permissions_classes = [IsAuthenticated]
    def perfom_create(self, serializer):
        serializer.save(author=self.request.user)


class ListPostAPIView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    search_fields = ["title", "description"]
    # filter_backends ekle
    # def get_queryset(self):
    #     return Post.objects.all()
    queryset = Post.objects.all()


class DetailPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"


class CommentCreateUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CommentCreateUpdateSerializer
    queryset = Comment.objects.all()


class CreateCommentApiView(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericAPIView
):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    permissions_classes = [IsCommentUserReadOnly]

    def perform_create(self, serializer):
        post_pk = self.kwargs.get("post_pk")
        post = get_object_or_404(Post, pk=post_pk)
        user = self.request.user
        comments = Comment.objects.filter(post=post, comment_owner=user)
        if comments.exists():
            raise ValidationError("Bir posta sadece bir yorum yazabilirsiniz.")
        serializer.save(post=post, comment_owner=user)

    # def post(self, request, slug, *args, **kwargs):
    #     post = get_object_or_404(Post, slug=slug)
    #     serializer = CreateCommentUpdateSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(author=request.user, parent=post)
    #         return Response(serializer.data, status=200)
    #     else:
    #         return Response({"errors": serializer.errors}, status=400)
