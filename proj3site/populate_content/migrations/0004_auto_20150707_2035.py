# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0003_house_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='history',
        ),
        migrations.AddField(
            model_name='region',
            name='history',
            field=models.TextField(null=True),
        ),
    ]
