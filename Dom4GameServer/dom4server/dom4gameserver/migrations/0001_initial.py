# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('servername', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=15, choices=[(b'NEW', b'New Game'), (b'PRETENDER', b'Game Accepting Pretenders'), (b'RUNNING', b'Game Running'), (b'STOPPED', b'Game Stopped'), (b'COMPLETE', b'Game Complete')])),
                ('timer', models.IntegerField(blank=True)),
                ('paused', models.BooleanField(default=False)),
                ('paused2', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('command', models.CharField(max_length=15, choices=[(b'RESET', b'Timer Reset'), (b'SETTIMER', b'Set Game Timer'), (b'PAUSE', b'Pause Game Timer'), (b'UNPAUSE', b'Restore Game Timer')])),
                ('arg1', models.CharField(max_length=25, blank=True)),
                ('status', models.CharField(default=b'NEW', max_length=15, choices=[(b'NEW', b'New Request'), (b'APPROVED', b'Request Approved'), (b'PROCESSED', b'Request Processed'), (b'DECLINED', b'Request Declined'), (b'CLOSED', b'Request Closed')])),
                ('requestDate', models.DateTimeField(auto_now_add=True)),
                ('approvedDate', models.DateTimeField(null=True, editable=False)),
                ('game', models.ForeignKey(to='dom4gameserver.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerCommand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('command', models.CharField(max_length=15, choices=[(b'RESET', b'Reset Timer'), (b'STOP', b'Stop Game'), (b'START', b'Start (or Restart) Game'), (b'SETTIMER', b'Set a Games Timer')])),
                ('arg1', models.CharField(max_length=25, blank=True)),
                ('status', models.CharField(max_length=15, choices=[(b'NEW', b'New Command'), (b'EXECUTING', b'Command being processed'), (b'EXECUTED', b'Command complete')])),
                ('game', models.ForeignKey(to='dom4gameserver.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='request',
            name='serverCommand',
            field=models.ForeignKey(blank=True, to='dom4gameserver.ServerCommand', null=True),
            preserve_default=True,
        ),
    ]
