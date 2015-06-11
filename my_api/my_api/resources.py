from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
