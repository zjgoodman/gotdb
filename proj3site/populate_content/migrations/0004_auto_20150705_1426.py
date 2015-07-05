# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('populate_content', '0003_remove_person_actor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Castle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='place',
            name='region',
        ),
        migrations.AddField(
            model_name='region',
            name='name',
            field=models.CharField(default='f', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.AddField(
            model_name='castle',
            name='region',
            field=models.ForeignKey(to='populate_content.Region'),
        ),
    ]
