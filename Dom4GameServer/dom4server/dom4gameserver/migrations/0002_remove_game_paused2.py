# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom4gameserver', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='paused2',
        ),
    ]
