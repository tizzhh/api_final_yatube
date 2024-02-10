from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=Follow.objects.all(), slug_field='username'
    )
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    # following = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('user',)

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Follow.objects.all(), fields=('user', 'following')
        #     )
        # ]
