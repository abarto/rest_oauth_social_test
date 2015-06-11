from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField, ReadOnlyField

from .models import Item, ItemGroup


class ItemSerializer(HyperlinkedModelSerializer):
    owner = HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Item
        fields = ('url', 'name', 'description', 'owner', 'mass')


class ItemGroupSerializer(HyperlinkedModelSerializer):
    owner = HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = ItemGroup
        fields = ('url', 'name', 'items', 'owner')
