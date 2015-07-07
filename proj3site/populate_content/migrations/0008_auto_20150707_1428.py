# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0007_auto_20150706_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_id', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('words', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='castle',
            name='castle_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='person_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='region_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='castle_name',
            field=models.ForeignKey(to='populate_content.Castle', null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='region_name',
            field=models.ForeignKey(to='populate_content.Region', null=True),
        ),
        migrations.AddField(
            model_name='castle',
            name='ruling_house',
            field=models.ForeignKey(to='populate_content.House', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='house_name',
            field=models.ForeignKey(to='populate_content.House', null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='ruling_house',
            field=models.ForeignKey(to='populate_content.House', null=True),
        ),
    ]
