# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PrivateChat, PrivateMessage
# Register your models here.
admin.site.register(PrivateChat)
admin.site.register(PrivateMessage)
