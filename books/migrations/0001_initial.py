# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=75)),
                ('owned', models.BooleanField()),
                ('to_read', models.BooleanField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('title', 'author')]),
        ),
    ]
