from django.urls import path, include

from rest_framework import routers

from .views import FollowViewSet, PostViewSet, CommentViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments',
                CommentViewSet,
                basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
