# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0008_auto_20150915_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='ranking',
            name='weighted_score',
        ),
        migrations.AddField(
            model_name='artist',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
