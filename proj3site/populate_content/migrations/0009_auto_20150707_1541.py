# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0008_auto_20150707_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_id', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to=b'')),
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
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name',)},
        ),
    ]
