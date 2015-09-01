# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(unique=True, max_length=300)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(unique=True, max_length=300)),
                ('start_date', models.DateField()),
                ('artists', models.ManyToManyField(related_name='festivals', to='stagegage.Artist')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(max_length=20, choices=[(b'avant garde', b'Avant Garde'), (b'blues', b'Blues'), (b'country', b'Country'), (b'electronic', b'Electronic'), (b'folk', b'Folk'), (b'hip hop', b'Hip Hop'), (b'jazz', b'Jazz'), (b'pop', b'Pop'), (b'r&b', b'R&B'), (b'rock', b'Rock')])),
                ('artist', models.ForeignKey(related_name='genres', to='stagegage.Artist')),
                ('user', models.ForeignKey(related_name='genres', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('score', models.FloatField()),
                ('artist', models.ForeignKey(related_name='rankings', to='stagegage.Artist')),
                ('festival', models.ForeignKey(related_name='rankings', to='stagegage.Festival')),
                ('user', models.ForeignKey(related_name='rankings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('artist', models.ForeignKey(related_name='reviews', to='stagegage.Artist')),
                ('festival', models.ForeignKey(related_name='reviews', to='stagegage.Festival')),
                ('user', models.ForeignKey(related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'artist', 'festival')]),
        ),
        migrations.AlterUniqueTogether(
            name='ranking',
            unique_together=set([('user', 'artist', 'festival')]),
        ),
    ]
