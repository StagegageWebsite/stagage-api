"""User model that just inherits from AbstractUser."""

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    """User model just inherists from AbstractUser for now.

    Can add more detail is necessary, but this is probably all we need.
    """
    def __unicode__(self):
        return self.username

# This is a post save hook that creates an auth token whenever a new user
# is created, for token auth.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)