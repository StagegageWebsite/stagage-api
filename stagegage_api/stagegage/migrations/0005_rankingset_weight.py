# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0004_auto_20150913_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='rankingset',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
