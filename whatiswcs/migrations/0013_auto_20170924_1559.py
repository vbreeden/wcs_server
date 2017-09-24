# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 19:59
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whatiswcs', '0012_auto_20170924_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dancer',
            name='other_dance_styles',
        ),
        migrations.AddField(
            model_name='dancer',
            name='other_dance_styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AMERICAN SLOW WALTZ', 'American Slow Waltz'), ('ARGENTINE TANGO', 'Argentine Tango'), ('BALBOA', 'Balboa'), ('BLUES', 'Blues'), ('BOLERO', 'Bolero'), ('CAROLINA SHAG', 'Carolina Shag'), ('CHA CHA', 'Cha Cha'), ('CHARLESTON', 'Charleston'), ('COLLEGIATE SHAG', 'Collegiate Shag'), ('COUNTRY TWO STEP', 'Country Two Step'), ('EAST COAST SWING', 'East Coast Swing'), ('FOXTROT', 'Foxtrot'), ('HUSTLE', 'Hustle'), ('JIVE', 'Jive'), ('KIZOMBA', 'Kizomba'), ('LINDY HOP', 'Lindy Hop'), ('MAMBO', 'Mambo'), ('MERENGUE', 'Merengue'), ('NIGHTCLUB TWO STEP', 'Nightclub Two Step'), ('QUICKSTEP', 'Quickstep'), ('RUMBA', 'Rumba'), ('SAMBA', 'Samba'), ('SALSA', 'Salsa'), ('TANGO', 'Tango'), ('TRIPLE TWO STEP', 'Triple Two Step'), ('VIENNESE WALTZ', 'Viennese Waltz'), ('ZOUK', 'Zouk'), ('OTHER', 'Other')], max_length=286, null=True),
        ),
        migrations.DeleteModel(
            name='OtherDance',
        ),
    ]
