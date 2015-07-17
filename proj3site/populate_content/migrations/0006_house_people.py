# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0005_person_region_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='people',
            field=models.ManyToManyField(to='populate_content.Person', blank=True),
        ),
    ]
