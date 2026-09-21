from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from accounts.managers import BenevolentUserManager


class BenevolentUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BenevolentUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):

    user = models.OneToOneField(
        BenevolentUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    inspiration_coins = models.PositiveIntegerField(default=0)
    supported_ideas = models.ManyToManyField(
        'ideas.Idea',
        related_name='supporters',
        verbose_name='Supported Ideas',
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
