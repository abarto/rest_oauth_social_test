from __future__ import absolute_import, unicode_literals

from rest_framework.viewsets import ModelViewSet

from .models import Item, ItemGroup
from .serializers import ItemSerializer, ItemGroup


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemGroupViewSet(ModelViewSet):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemSerializer
