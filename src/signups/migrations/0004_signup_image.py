# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0003_signup_edited_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='image',
            field=models.URLField(default='https://vignette2.wikia.nocookie.net/lotr/images/b/b6/Aragorn_profile.jpg/revision/latest?cb=20170121121423'),
            preserve_default=False,
        ),
    ]
