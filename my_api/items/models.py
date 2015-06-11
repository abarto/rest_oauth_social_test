from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Item(TimeStampedModel, models.Model):
    name = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('owner'))
    mass = models.FloatField(_('mass'), blank=True, null=True)


class ItemGroup(TimeStampedModel, models.Model):
    name = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('owner'))
    items = models.ManyToManyField(Item, verbose_name=_('items'))
