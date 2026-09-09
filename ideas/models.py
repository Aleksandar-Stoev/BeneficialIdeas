from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Idea(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING',
        REVIEW = 'REVIEW',
        APPROVED = 'APPROVED',

    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Idea title',
        help_text=(
            'Enter a short and catchy title (minimum 5 characters).'
        ),
    )

    description = models.TextField(
        verbose_name='Description',
        help_text='Describe how this idea will improve the world.',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ideas',
        verbose_name='Author',
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='ideas',
        verbose_name='Category',
    )

    inspiration_coins = models.PositiveIntegerField(
        default=0,
        verbose_name='Collected inspiration_coins',
    )

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        verbose_name='Idea status',
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Creation date'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Last edit'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'
        ordering = ['-created_at']
