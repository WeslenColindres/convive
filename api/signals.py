from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class CreateAuthTokenReceiver:
    def __init__(self):
        pass

    def dispatch(self, sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)