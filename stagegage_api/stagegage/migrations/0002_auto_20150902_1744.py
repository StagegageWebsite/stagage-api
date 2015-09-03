# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stagegage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rankingset',
            name='festival',
            field=models.ForeignKey(related_name='rankings_set', to='stagegage.Festival'),
        ),
        migrations.AddField(
            model_name='rankingset',
            name='user',
            field=models.ForeignKey(related_name='rankings_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ranking',
            name='artist',
            field=models.ForeignKey(to='stagegage.Artist'),
        ),
        migrations.AddField(
            model_name='ranking',
            name='ranking_set',
            field=models.ForeignKey(related_name='rankings', to='stagegage.RankingSet'),
        ),
        migrations.AddField(
            model_name='genre',
            name='artist',
            field=models.ForeignKey(related_name='genres', to='stagegage.Artist'),
        ),
        migrations.AddField(
            model_name='genre',
            name='user',
            field=models.ForeignKey(related_name='genres', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='festival',
            name='artists',
            field=models.ManyToManyField(related_name='festivals', to='stagegage.Artist'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'artist', 'festival')]),
        ),
        migrations.AlterUniqueTogether(
            name='rankingset',
            unique_together=set([('user', 'festival')]),
        ),
    ]
