# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom4gameserver', '0005_auto_20150207_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='maptype',
            field=models.IntegerField(choices=[(1, b'Random Map'), (2, b'Pregenerated Map')]),
            preserve_default=True,
        ),
    ]
