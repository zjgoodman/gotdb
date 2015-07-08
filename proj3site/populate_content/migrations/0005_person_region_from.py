# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0004_auto_20150707_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='region_from',
            field=models.ForeignKey(to='populate_content.Region', null=True),
        ),
    ]
