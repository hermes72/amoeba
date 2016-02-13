# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('TimeStamp', models.DateTimeField(verbose_name='')),
                ('Genre', models.CharField(max_length=20)),
                ('Venue', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=50)),
                ('Postscript', models.CharField(max_length=50)),
                ('Links', models.CharField(max_length=200)),
                ('Updated', models.BooleanField()),
            ],
        ),
    ]
