# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom4gameserver', '0003_auto_20150201_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='extraswitches',
            field=models.CharField(max_length=3000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='mapfile',
            field=models.CharField(default='', max_length=64, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='maptype',
            field=models.IntegerField(default=1, choices=[(1, b'Random Map'), (2, b'Middle Age')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='masterpass',
            field=models.CharField(default='nopass', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='randmap',
            field=models.IntegerField(default=15, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='command',
            field=models.CharField(max_length=15, choices=[(b'RESET', b'Timer Reset'), (b'SETTIMER', b'Set Game Timer'), (b'PAUSE', b'Pause Game Timer'), (b'UNPAUSE', b'Restore Game Timer'), (b'NEWGAME', b'Request New Game')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servercommand',
            name='command',
            field=models.CharField(max_length=15, choices=[(b'RESET', b'Reset Timer'), (b'STOP', b'Stop Game'), (b'START', b'Start (or Restart) Game'), (b'SETTIMER', b'Set a Games Timer'), (b'CREATEGAME', b'Create the Game Script')]),
            preserve_default=True,
        ),
    ]
