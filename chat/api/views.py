from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication

from profiles.models import Profile
from chat.models import PrivateChat, PrivateMessage

from rest_framework.views import APIView

from profiles.api.serializers import ProfileSerializer
from .serializers import ChatSerializer

class ChatView(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    model = PrivateChat
    queryset = PrivateChat.objects.all()

class ChatApi(APIView):
    def get(self, request, *args, **kwargs):
        usr = request.user
        #try:
        profile1 = Profile.objects.get(user=usr)
        profile2 = Profile.objects.get(user=kwargs['p'])
        chat = PrivateChat.objects.filter(profiles=profile1).get(profiles=profile2)
        serializer = ChatSerializer(chat, context={'request': request})
        return JsonResponse(serializer.data)
        #except:
            #return JsonResponse({'message' : 'noProfile'})
