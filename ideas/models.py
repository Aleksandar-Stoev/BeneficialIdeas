from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models, transaction
from django.db.models import F

User = get_user_model()


class Idea(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        REVIEW = 'REVIEW', 'In Review'
        APPROVED = 'APPROVED', 'Approved'

    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Idea title',
        help_text=(
            'Enter a short and catchy title (minimum 5 characters).'
        ),
        validators=[MinLengthValidator(2)]
    )

    description = models.TextField(
        verbose_name='Description',
        help_text='Describe the benefits of your idea.',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ideas',
        verbose_name='Author',
    )

    category = models.ManyToManyField(
        'categories.Category',
        related_name='ideas',
        verbose_name='Category',
        blank=True,
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

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if is_new:
            with transaction.atomic():
                super().save(*args, **kwargs)
                if self.author and hasattr(self.author, 'profile'):
                    profile = self.author.profile
                    profile.inspiration_coins = F('inspiration_coins') + 100
                    profile.save(update_fields=['inspiration_coins'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'
        ordering = ['-created_at']
