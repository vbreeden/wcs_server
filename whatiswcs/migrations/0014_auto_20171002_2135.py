# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 01:35
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whatiswcs', '0013_auto_20171002_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songanddancer',
            name='other_dance_styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('SMOOTH_BALLROOM', 'Smooth/Standard Ballroom Dances'), ('RHYTHM_BALLROOM', 'Rhythm/Latin Dances'), ('COUNTRY', 'Country Dances'), ('BLUES', 'Blues'), ('CLUB', 'Club Dances'), ('OTHER', 'Other Styles')], max_length=56, null=True),
        ),
    ]
