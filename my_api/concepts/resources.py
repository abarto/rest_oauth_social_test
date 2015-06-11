from __future__ import absolute_import, unicode_literals

from rest_framework.viewsets import ModelViewSet

from .models import Concept
from .serializers import ConceptSerializer


class ConceptViewSet(ModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
