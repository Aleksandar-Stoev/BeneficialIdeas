from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from BeneficialIdeas import settings
from accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)
