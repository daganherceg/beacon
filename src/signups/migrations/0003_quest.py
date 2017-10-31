# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_remove_signup_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quest_id', models.IntegerField(default=0)),
                ('quest_name', models.CharField(max_length=120, null=True, blank=True)),
                ('quest_contents', models.CharField(max_length=200, null=True)),
                ('quest_owner', models.ForeignKey(to='signups.SignUp')),
            ],
        ),
    ]
