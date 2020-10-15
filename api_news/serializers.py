from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Create news post"""

    class Meta:
        model = Post
        fields = [
            "url",
            "id",
            "title",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]


class CommentSerializer(serializers.ModelSerializer):
    """Create comment for news post"""

    class Meta:
        model = Comment
        fields = ["url", "id", "post", "author_name", "content", "creation_date"]


class PostUpvoteSerializer(serializers.ModelSerializer):
    """Upvote post"""

    class Meta:
        model = Post
        fields = ["url", "id", "title", "amount_of_upvotes", "creation_date"]

    def update(self, instance, validated_data):
        instance.amount_of_upvotes += 1
        instance.save()
        return instance
