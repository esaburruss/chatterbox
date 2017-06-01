# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 

# Create your models here.
class Profile(models.Model):
    GENDER = (
        (0, 'Female'),
        (1, 'Male'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(default=0, choices=GENDER)
    def __str__(self):
        return self.user.first_name
    def firstName(self):
        return self.user.first_name
    def lastName(self):
        return self.user.last_name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
