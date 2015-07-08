# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0002_auto_20150707_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='history',
            field=models.TextField(null=True),
        ),
    ]
