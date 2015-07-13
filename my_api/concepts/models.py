from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Concept(TimeStampedModel, models.Model):
    name = models.CharField(_('title'), max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name
