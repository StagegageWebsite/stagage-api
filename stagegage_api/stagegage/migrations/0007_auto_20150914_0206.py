# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0006_auto_20150914_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='weighted_score',
            field=models.FloatField(null=True),
        ),
    ]
