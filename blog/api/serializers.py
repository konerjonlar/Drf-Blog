from blog.models import Comment, Post
from django.db.models import fields
from rest_framework import serializers

# Base Serializer oluşturulacak.


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment

        exclude = ["parent"]


class PostSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="blog:detail_post", lookup_field="pk")
    # username = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post

        fields = [
            "id",
            "author",
            "title",
            "comments",
            "description",
            "slug",
            "image",
            "created_at",
            "updated_at",
            "is_active",
        ]

    # def get_author(self, obj):
    #     # print(obj)
    #     return str(obj.user.username)


class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "content", "is_active"]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["parent", "content"]
