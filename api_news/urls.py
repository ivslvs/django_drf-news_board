from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostUpvoteView, PostViewSet, CommentViewSet


router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("posts/<int:pk>/upvote/", PostUpvoteView.as_view()),
]

urlpatterns += [path("", include(router.urls))]
