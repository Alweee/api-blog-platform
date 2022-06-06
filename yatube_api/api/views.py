from django.shortcuts import get_object_or_404

from rest_framework import filters, permissions, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post, User
from .permissions import OwnerOrReadOnly, OwnerOrReadOnly2, ReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostGetViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly2,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly2,)

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('post_pk')
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=post_pk)
        )

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_pk)
        new_queryset = post.comments.all()
        return new_queryset

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class FollowViewSet(PostGetViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, OwnerOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        new_queryset = user.follower.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
