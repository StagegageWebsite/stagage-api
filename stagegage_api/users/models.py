from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from oauth2_provider.models import Application
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver



class User(AbstractUser):

    def __unicode__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_client(sender, instance=None, created=False, **kwargs):
    """
    Intended to be used as a receiver function for a `post_save` signal on User model
    Creates client_id and client_secret for authenticated users
    """
    if created:
        Application.objects.create(user=instance,
                                   client_type=Application.CLIENT_CONFIDENTIAL,
                                   authorization_grant_type=Application.GRANT_PASSWORD)