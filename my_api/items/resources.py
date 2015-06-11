from __future__ import absolute_import, unicode_literals

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Item, ItemGroup
from .permissions import IsOwnerOrReadOnly
from .serializers import ItemSerializer, ItemGroupSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class ItemGroupViewSet(ModelViewSet):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupSerializer

    permission_classes = (
        IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
