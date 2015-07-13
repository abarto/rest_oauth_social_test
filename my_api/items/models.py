from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Item(TimeStampedModel, models.Model):
    name = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    owner = models.ForeignKey('auth.User', verbose_name=_('owner'), related_name='items')
    mass = models.FloatField(_('mass'), blank=True, null=True)

    def __str__(self):
        return self.name


class ItemGroup(TimeStampedModel, models.Model):
    name = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    owner = models.ForeignKey('auth.User', verbose_name=_('owner'), related_name='itemgroups')
    items = models.ManyToManyField(Item, verbose_name=_('items'))

    def __str__(self):
        return self.name
