# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0005_auto_20150706_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='castle',
            old_name='region',
            new_name='region_name',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='region',
            new_name='region_name',
        ),
        migrations.AddField(
            model_name='region',
            name='capital_name',
            field=models.ForeignKey(to='populate_content.Castle', null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='ruling_house',
            field=models.ForeignKey(to='populate_content.House', null=True),
        ),
    ]
