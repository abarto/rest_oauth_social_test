from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

from items.models import Item, ItemGroup

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups', 'items', 'itemgroups')


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
