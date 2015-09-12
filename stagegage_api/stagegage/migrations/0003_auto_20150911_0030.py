# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stagegage', '0002_auto_20150902_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankingset',
            name='festival',
            field=models.ForeignKey(related_name='ranking_set', to='stagegage.Festival'),
        ),
        migrations.AlterField(
            model_name='rankingset',
            name='user',
            field=models.ForeignKey(related_name='ranking_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
