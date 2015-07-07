# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0004_auto_20150705_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=200)),
                ('words', models.CharField(null=True, max_length=300)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='castle',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('first_name',)},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='castle',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='castle',
            name='ruling_lord',
            field=models.ForeignKey(to='populate_content.Person', null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='ruling_lord',
            field=models.ForeignKey(to='populate_content.Person', null=True),
        ),
        migrations.AlterField(
            model_name='castle',
            name='name',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='castle',
            name='region',
            field=models.ForeignKey(to='populate_content.Region', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='titles',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='region',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='castle_name',
            field=models.ForeignKey(to='populate_content.Castle', null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='region',
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
    ]
