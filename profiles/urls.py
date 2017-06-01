from django.conf.urls import url, include
from rest_framework import routers

from .api.views import UserView, ProfileView, ProfileApi, login_user, logout_user, get_auth_token
from rest_framework.authtoken import views as rest_framework_views

router = routers.DefaultRouter()
#router.register(r'users', UserView, 'list')
router.register(r'profiles', ProfileView, 'list')

app_name = 'profiles'
urlpatterns = [
    url(r'^api/profile/$', ProfileApi.as_view(), name="profile"),
    url(r'^api/', include(router.urls)),
    url(r'^api/login/$', login_user, name='login'),
    url(r'^api/logout/$', logout_user, name='logout'),
    url(r'^api/token/$', get_auth_token, name='token'),
    url(r'^api/get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
