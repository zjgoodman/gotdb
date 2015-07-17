# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0007_auto_20150714_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='former_castles_controlled',
            field=models.ManyToManyField(related_name='house_former_castles_controlled', to='populate_content.Castle', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='castles_controlled',
            field=models.ManyToManyField(related_name='person_castles_owned', to='populate_content.Castle', blank=True),
        ),
        migrations.AddField(
            model_name='region',
            name='ruling_lord',
            field=models.ForeignKey(to='populate_content.Person', null=True),
        ),
    ]
