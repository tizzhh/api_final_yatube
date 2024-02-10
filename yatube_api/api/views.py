from django.core.exceptions import BadRequest
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Follow, Group, Post


class IsRequestUserAuthOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )


class GroupView(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsRequestUserAuthOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsRequestUserAuthOwnerOrReadOnly,)

    def get_queryset(self):
        return self.get_post_obj(self.kwargs.get('post_id')).comments.all()

    def perform_create(self, serializer):
        post = self.get_post_obj(self.kwargs.get('post_id'))
        serializer.save(post=post, author=self.request.user)

    @staticmethod
    def get_post_obj(pk: int):
        return get_object_or_404(Post, pk=pk)


class FollowView(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.following.all()

    def perform_create(self, serializer):
        user_to_follow = serializer.validated_data['following']
        if user_to_follow == self.request.user:
            raise BadRequest('Cannot follow oneself')
        already_followed = Follow.objects.filter(
            user=self.request.user, following=user_to_follow
        )
        if len(already_followed) != 0:
            raise BadRequest('User is already being followed')
        serializer.save(user=self.request.user)
