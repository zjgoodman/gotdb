# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0006_house_people'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name')},
        ),
        migrations.RenameField(
            model_name='castle',
            old_name='ruling_house',
            new_name='primary_house',
        ),
        migrations.RenameField(
            model_name='castle',
            old_name='ruling_lord',
            new_name='primary_lord',
        ),
        migrations.RemoveField(
            model_name='house',
            name='castle_name',
        ),
        migrations.RemoveField(
            model_name='house',
            name='people',
        ),
        migrations.RemoveField(
            model_name='house',
            name='region_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='house_name',
        ),
        migrations.RemoveField(
            model_name='region',
            name='ruling_lord',
        ),
        migrations.AddField(
            model_name='castle',
            name='previous_houses',
            field=models.ManyToManyField(related_name='castle_previous_houses', blank=True, to='populate_content.House'),
        ),
        migrations.AddField(
            model_name='castle',
            name='previous_lords',
            field=models.ManyToManyField(related_name='castle_previous_lords', blank=True, to='populate_content.Person'),
        ),
        migrations.AddField(
            model_name='house',
            name='castles_controlled',
            field=models.ManyToManyField(related_name='house_castles_controlled', blank=True, to='populate_content.Castle'),
        ),
        migrations.AddField(
            model_name='house',
            name='members',
            field=models.ManyToManyField(related_name='house_family_members', blank=True, to='populate_content.Person'),
        ),
        migrations.AddField(
            model_name='house',
            name='sigil',
            field=models.CharField(null=True, max_length=300),
        ),
        migrations.AddField(
            model_name='person',
            name='cause_of_death',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='houses',
            field=models.ManyToManyField(related_name='person_houses', blank=True, to='populate_content.House'),
        ),
        migrations.AddField(
            model_name='person',
            name='killer',
            field=models.ForeignKey(null=True, to='populate_content.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='loyal_to',
            field=models.ManyToManyField(related_name='person_houses_loyal_to', blank=True, to='populate_content.House'),
        ),
        migrations.AddField(
            model_name='region',
            name='other_castles',
            field=models.ManyToManyField(related_name='castles_in_region', blank=True, to='populate_content.Castle'),
        ),
        migrations.AddField(
            model_name='region',
            name='previous_ruling_houses',
            field=models.ManyToManyField(related_name='previous_ruling_houses', blank=True, to='populate_content.House'),
        ),
        migrations.AddField(
            model_name='region',
            name='resident_houses',
            field=models.ManyToManyField(related_name='houses_in_this_region', blank=True, to='populate_content.House'),
        ),
        migrations.AlterField(
            model_name='person',
            name='titles',
            field=models.TextField(null=True),
        ),
    ]
