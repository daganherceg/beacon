# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0008_auto_20171029_2113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
