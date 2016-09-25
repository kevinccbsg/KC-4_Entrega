from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.serializers import UserSerializer
from users.permissions import UserPermission

__author__ = 'kevinccbsg'


class UserListAPI(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)


class UserDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

