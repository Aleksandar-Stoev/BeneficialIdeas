from django.db import models
from ideas.models import Idea


class Resource(models.Model):
    idea = models.ForeignKey(
        Idea,
        on_delete=models.CASCADE,
        related_name='resources',
    )
    name = models.CharField(
        max_length=100, verbose_name='Required resource'
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Required quantity'
    )
    is_secured = models.BooleanField(
        default=False, verbose_name='Is it provided?'
    )
