# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20150611_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(related_name='items', verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itemgroup',
            name='owner',
            field=models.ForeignKey(related_name='itemgroups', verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
