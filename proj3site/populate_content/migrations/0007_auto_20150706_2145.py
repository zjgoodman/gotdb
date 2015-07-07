# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0006_auto_20150706_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='castle_name',
        ),
        migrations.RemoveField(
            model_name='house',
            name='region_name',
        ),
        migrations.RemoveField(
            model_name='castle',
            name='ruling_house',
        ),
        migrations.RemoveField(
            model_name='person',
            name='house_name',
        ),
        migrations.RemoveField(
            model_name='region',
            name='ruling_house',
        ),
        migrations.DeleteModel(
            name='House',
        ),
    ]
