# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('iso2', models.CharField(unique=True, max_length=2, verbose_name='ISO 3166-1 Alpha 2 Name')),
                ('iso3', models.CharField(unique=True, max_length=3, verbose_name='ISO 3166-1 Alpha 3 Name')),
                ('name', models.CharField(unique=True, max_length=128, verbose_name='Country Name')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
                'ordering': ('iso2', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('abbr', models.CharField(max_length=10, verbose_name='Territory Abbreviation')),
                ('name', models.CharField(max_length=128, verbose_name='Territory Name')),
                ('country', models.ForeignKey(related_name='territories', to='locality.Country', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Territories',
                'verbose_name': 'Territory',
                'ordering': ('abbr', 'name'),
            },
            bases=(models.Model,),
        ),
    ]
