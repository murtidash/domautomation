# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom4gameserver', '0002_remove_game_paused2'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='age',
            field=models.IntegerField(default=1, choices=[(1, b'Early Age'), (2, b'Middle Age'), (3, b'Late Age')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='notes',
            field=models.CharField(max_length=3000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='port',
            field=models.IntegerField(default=1234, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='throne1',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='throne2',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='throne3',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='thrones',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='thronewin',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
