# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0005_rankingset_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rankingset',
            name='weight',
        ),
        migrations.AddField(
            model_name='ranking',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ranking',
            name='weighted_score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='artist',
            field=models.ForeignKey(related_name='rankings', to='stagegage.Artist'),
        ),
    ]
