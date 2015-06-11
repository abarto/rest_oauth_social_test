from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Concept


class ConceptSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Concept
        fields = ('url', 'name', 'parent')
