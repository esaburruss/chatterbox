from django.conf.urls import url, include
from rest_framework import routers

from .api.views import UserView, ProfileView, login_user, logout_user, gettoken

router = routers.DefaultRouter()
#router.register(r'users', UserView, 'list')
router.register(r'profiles', ProfileView, 'list')

app_name = 'profiles'
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/login/$', login_user, name='login'),
    url(r'^api/logout/$', logout_user, name='logout'),
    url(r'^api/token/$', gettoken, name='token'),
]
