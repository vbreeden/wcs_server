# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 03:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django_countries.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whatiswcs', '0003_auto_20170927_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongAndDancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('artist', models.CharField(max_length=128)),
                ('features', models.TextField(blank=True, null=True)),
                ('song_url', models.TextField(blank=True, null=True)),
                ('primary_dance_role', models.CharField(choices=[('LEAD', 'lead'), ('FOLLOW', 'follow'), ('BOTH', 'both')], default='LEAD', max_length=6)),
                ('competitive_level', models.CharField(choices=[('SOCIAL', 'Social Only'), ('NEWCOMER', 'Newcomer'), ('NOVICE', 'Novice'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced'), ('ALLSTAR', 'All-Star')], default='SOCIAL', max_length=12)),
                ('years_dancing', models.IntegerField(choices=[(0, '< 1'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10+')], default=0)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(6)])),
                ('dj', models.BooleanField()),
                ('teacher', models.BooleanField(default=False)),
                ('other_dances', models.BooleanField()),
                ('other_dance_styles', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AMERICAN SLOW WALTZ', 'American Slow Waltz'), ('ARGENTINE TANGO', 'Argentine Tango'), ('BALBOA', 'Balboa'), ('BLUES', 'Blues'), ('BOLERO', 'Bolero'), ('CAROLINA SHAG', 'Carolina Shag'), ('CHA CHA', 'Cha Cha'), ('CHARLESTON', 'Charleston'), ('COLLEGIATE SHAG', 'Collegiate Shag'), ('COUNTRY TWO STEP', 'Country Two Step'), ('EAST COAST SWING', 'East Coast Swing'), ('FOXTROT', 'Foxtrot'), ('HUSTLE', 'Hustle'), ('JIVE', 'Jive'), ('KIZOMBA', 'Kizomba'), ('LINDY HOP', 'Lindy Hop'), ('MAMBO', 'Mambo'), ('MERENGUE', 'Merengue'), ('NIGHTCLUB TWO STEP', 'Nightclub Two Step'), ('QUICKSTEP', 'Quickstep'), ('RUMBA', 'Rumba'), ('SAMBA', 'Samba'), ('SALSA', 'Salsa'), ('TANGO', 'Tango'), ('TRIPLE TWO STEP', 'Triple Two Step'), ('VIENNESE WALTZ', 'Viennese Waltz'), ('ZOUK', 'Zouk'), ('OTHER', 'Other')], max_length=286, null=True)),
                ('region', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]