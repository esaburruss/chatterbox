# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiles.models import Profile

# Create your models here.
class PrivateChat(models.Model):
    profiles = models.ManyToManyField(Profile, related_name='chats')

    def clean(self, *args, **kwargs):
        if self.profiles.count() > 2:
            raise ValidationError("You can't assign more than two profiles to a chat")
        super(PrivateChat, self).clean(*args, **kwargs)

    def __str__(self):
        str = ''
        for p in self.profiles.all():
            str += p.firstName()
        return str
    def get_messages(self):
        return PrivateMessage.objects.filter(chat=self).order_by('timestamp')

class PrivateMessage(models.Model):
    timestamp = models.DateTimeField('timestamp', editable=False, auto_now_add=True)
    chat = models.ForeignKey(PrivateChat, related_name='messages')
    profile_from = models.ForeignKey(Profile, related_name='messages')
    message_body = models.TextField()

    def __str__(self):
        return self.profile_from.firstName() + ': ' + unicode(self.timestamp)
