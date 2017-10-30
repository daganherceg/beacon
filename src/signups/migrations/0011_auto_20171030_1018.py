# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0010_beacon_hero_quest'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
