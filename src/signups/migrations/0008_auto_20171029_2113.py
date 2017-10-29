# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0007_auto_20171029_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='field',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.URLField(default=b'https://a3-images.myspacecdn.com/images03/1/240e42b5d9ce48a78983961e7fcb3c39/600x600.jpg', max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='image',
            field=models.URLField(max_length=500, blank=True),
        ),
    ]
