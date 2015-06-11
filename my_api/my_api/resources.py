from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
