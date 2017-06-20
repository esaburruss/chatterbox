from django.conf.urls import url, include
from rest_framework import routers
from .api.views import ChatApi

app_name = 'chat'
urlpatterns = [
    url(r'^api/chat/(?P<p>[0-9])/$', ChatApi.as_view(), name="chat"),
]
