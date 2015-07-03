# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0002_auto_20150703_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='actor_name',
        ),
    ]
