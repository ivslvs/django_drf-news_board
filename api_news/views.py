from rest_framework.generics import UpdateAPIView
from .serializers import PostSerializer, CommentSerializer, PostUpvoteSerializer
from .models import Post, Comment
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    """Create news post"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Create comment fot news post """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostUpvoteView(UpdateAPIView):
    """Upvote post"""

    queryset = Post.objects.all()
    serializer_class = PostUpvoteSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.data["id"])
