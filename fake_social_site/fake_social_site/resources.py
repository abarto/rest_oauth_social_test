from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer


class UserViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
