from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from profiles.models import Profile
from django.views.csrf import csrf_failure

from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer, ProfileSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    model = Profile
    queryset = Profile.objects.all()

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    #print(request)
    user = authenticate(username=username, password=password)
    #print(get_token(request))
    if user is not None:
        # the password verified for the user
        if user.is_active:
            #print(get_token(request))
            login(request, user)
            token = get_token(request)
            print(token)
            return JsonResponse({'login':1,'username':user.username,'pk':user.pk,'csrftoken':token})
    else:
        return JsonResponse({'login':0})

def logout_user(request):
    logout(request)
    token = get_token(request)
    print(token)
    return JsonResponse({'login':0,'csrftoken':token})
