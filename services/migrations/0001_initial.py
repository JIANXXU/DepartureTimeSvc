# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartureTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('agencyName', models.CharField(default=b'', max_length=100, blank=True)),
                ('routeName', models.CharField(default=b'', max_length=100, blank=True)),
                ('stopName', models.CharField(default=b'', max_length=100, blank=True)),
                ('stopCode', models.IntegerField(default=0)),
                ('nextDepartureTime', models.IntegerField(default=-1)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
