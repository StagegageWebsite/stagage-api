# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0010_auto_20150915_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='score',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
