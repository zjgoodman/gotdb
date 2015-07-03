# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='title',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='df', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='titles',
            field=models.CharField(default='3', max_length=200),
            preserve_default=False,
        ),
    ]
