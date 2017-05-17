# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

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
