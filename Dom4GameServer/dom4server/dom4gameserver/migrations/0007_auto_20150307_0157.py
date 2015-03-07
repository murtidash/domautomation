# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom4gameserver', '0006_auto_20150209_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='mapfile',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='throne1',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='throne2',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='throne3',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='thronewin',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='command',
            field=models.CharField(max_length=15, choices=[(b'RESET', b'Timer Reset'), (b'SETTIMER', b'Set Game Timer'), (b'PAUSE', b'Pause Game Timer'), (b'UNPAUSE', b'Restore Game Timer'), (b'NEWGAME', b'Request New Game'), (b'STARTGAME', b'Start Pending Game')]),
            preserve_default=True,
        ),
    ]
