from rest_framework import serializers
from profiles.models import Profile
from django.contrib.auth.models import User
from profiles.api.serializers import ProfileSerializer
from chat.models import PrivateChat, PrivateMessage

class MessageSerializer(serializers.ModelSerializer):
    #_profile_from = serializers.SerializerMethodField()
    class Meta:
        model = PrivateMessage
        fields = ('message_body', 'profile_from', 'timestamp')
        #ordering = ['timestamp']
    def get__profile_from(self, obj):
        return obj.profile_from.pk

class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    #profiles = ProfileSerializer(Profile)
    profile = serializers.SerializerMethodField()
    class Meta:
        model = PrivateChat
        fields = ('profile', 'messages')
    def get_profile(self, obj, *args, **kwargs):
        p = self.context['request'].user.profile
        serializer = ProfileSerializer(obj.profiles.exclude(id=p.pk).get())
        return serializer.data

    def _get_messages(self, obj):
        print obj
        serializer = MessageSerializer(obj.messages, many=True)
        return serializer.data
