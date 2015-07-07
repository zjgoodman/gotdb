# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0009_auto_20150707_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='photo',
        ),
    ]
