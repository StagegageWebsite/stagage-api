# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0009_auto_20150915_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
