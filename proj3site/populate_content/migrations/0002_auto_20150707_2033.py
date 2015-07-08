# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='castle',
            name='history',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='actor',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
