from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from profiles.models import Profile
from django.views.csrf import csrf_failure
from rest_framework.views import APIView

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

class ProfileApi(APIView):
    #permission_classes = (TokenAuthentication,)
    def get(self, request, *args, **kwargs):
        usr = request.user
        try:
            profile = Profile.objects.get(user=usr)
            print(profile)
            serializer = ProfileSerializer(profile)
            return JsonResponse(serializer.data)
        except:
            return JsonResponse({'message' : 'noProfile'})


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


def get_auth_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            return JsonResponse({'login':1,'username':user.username,'pk':user.pk,'token':token})
    return JsonResponse({'login':0})

def logout_user(request):
    logout(request)
    token = get_token(request)
    print(token)
    return JsonResponse({'login':0,'csrftoken':token})

def gettoken(request):
    token = get_token(request)
    print(token)
    return JsonResponse({'login':0,'csrftoken':token})
