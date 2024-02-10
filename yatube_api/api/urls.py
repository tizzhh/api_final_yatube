from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentView, FollowView, GroupView, PostView

api_v1_router = SimpleRouter()
api_v1_router.register(r'groups', GroupView, basename='groups')
api_v1_router.register(r'posts', PostView, basename='posts')
api_v1_router.register(r'follow', FollowView, basename='follow')
api_v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentView, basename='comments'
)

urlpatterns = [
    path('v1/', include(api_v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
