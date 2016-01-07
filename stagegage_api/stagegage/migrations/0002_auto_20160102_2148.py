# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='artist',
            field=models.ForeignKey(related_name='artists', to='stagegage.Artist'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='festival',
            field=models.ForeignKey(related_name='festivals', to='stagegage.Festival'),
        ),
    ]
