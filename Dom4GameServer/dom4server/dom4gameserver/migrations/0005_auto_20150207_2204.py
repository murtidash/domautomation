# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dom4gameserver', '0004_auto_20150207_2001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'permissions': (('approve_requests', 'Can Approve Requests'),)},
        ),
    ]
