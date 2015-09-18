# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0007_auto_20150914_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='weighted_score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rankingset',
            name='festival',
            field=models.ForeignKey(related_name='ranking_sets', to='stagegage.Festival'),
        ),
        migrations.AlterField(
            model_name='rankingset',
            name='user',
            field=models.ForeignKey(related_name='ranking_sets', to=settings.AUTH_USER_MODEL),
        ),
    ]
