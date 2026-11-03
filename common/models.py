from django.contrib.auth import get_user_model
from django.db import models
from ideas.models import Idea

User = get_user_model()


class Comment(models.Model):
    idea = models.ForeignKey(
        Idea, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField(max_length=300, verbose_name='Comment text')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.idea}'
