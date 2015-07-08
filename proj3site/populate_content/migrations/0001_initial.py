# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_id', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('bio', models.TextField(null=True)),
                ('responsibilities', models.TextField(null=True)),
                ('num_commits', models.IntegerField(null=True)),
                ('num_issues', models.IntegerField(null=True)),
                ('num_unit_tests', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Castle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('castle_id', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_id', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('words', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(null=True)),
                ('castle_name', models.ForeignKey(to='populate_content.Castle', null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_id', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('titles', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('bio', models.TextField(null=True)),
                ('house_name', models.ForeignKey(to='populate_content.House', null=True)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_id', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('capital_name', models.ForeignKey(to='populate_content.Castle', null=True)),
                ('ruling_house', models.ForeignKey(to='populate_content.House', null=True)),
                ('ruling_lord', models.ForeignKey(to='populate_content.Person', null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='house',
            name='region_name',
            field=models.ForeignKey(to='populate_content.Region', null=True),
        ),
        migrations.AddField(
            model_name='castle',
            name='region_name',
            field=models.ForeignKey(to='populate_content.Region', null=True),
        ),
        migrations.AddField(
            model_name='castle',
            name='ruling_house',
            field=models.ForeignKey(to='populate_content.House', null=True),
        ),
        migrations.AddField(
            model_name='castle',
            name='ruling_lord',
            field=models.ForeignKey(to='populate_content.Person', null=True),
        ),
    ]
