# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatiswcs', '0013_auto_20170924_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dancer',
            name='song',
        ),
        migrations.AddField(
            model_name='dancer',
            name='song',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='whatiswcs.Song'),
        ),
    ]
