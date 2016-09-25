from django.conf.urls import url
from users.views import LoginView, LogoutView, SignUpView
from users.api import UserListAPI, UserDetailAPI

urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$',
        LogoutView.as_view(), name='users_logout'),
    url(r'^signup$', SignUpView.as_view(), name='signup'),

    # API
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='users_view'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$',
        UserDetailAPI.as_view(), name='user_detail_view')
]
