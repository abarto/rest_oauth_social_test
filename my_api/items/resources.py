from __future__ import absolute_import, unicode_literals

from rest_framework.viewsets import ModelViewSet

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
