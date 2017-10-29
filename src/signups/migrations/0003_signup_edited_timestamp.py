# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_remove_signup_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='edited_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 13, 23, 14, 612633, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
