# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0003_auto_20150911_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='user',
        ),
        migrations.AddField(
            model_name='genre',
            name='review',
            field=models.ForeignKey(related_name='genres', default=None, to='stagegage.Review'),
            preserve_default=False,
        ),
    ]
