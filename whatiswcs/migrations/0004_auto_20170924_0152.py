# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatiswcs', '0003_auto_20170924_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='competitive_level',
            field=models.CharField(choices=[('SOCIAL', 'Social Only'), ('NEWCOMER', 'Newcomer'), ('NOVICE', 'Novice'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced'), ('ALLSTAR', 'Allstar')], default='SOCIAL', max_length=12),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='primary_dance_role',
            field=models.CharField(choices=[('LEAD', 'lead'), ('FOLLOW', 'follow'), ('BOTH', 'both')], default='LEAD', max_length=6),
        ),
    ]
