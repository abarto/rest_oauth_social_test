from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Item, ItemGroup


class ItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url', 'name', 'description', 'owner', 'mass')


class ItemGroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ItemGroup
        fields = ('url', 'name', 'items')
