from django.db import models


class Post(models.Model):
    """News post"""

    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now=True, editable=False)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)


class Comment(models.Model):
    """Post's comment"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
