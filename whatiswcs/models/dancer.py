from django.db import models
from django.core.validators import MinValueValidator
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from .song import Song

# Dancers may primarily lead, follow, or regularly dance both roles
PRIMARY_DANCE_ROLE_CHOICES = (
    ('LEAD', 'lead'),
    ('FOLLOW', 'follow'),
    ('BOTH', 'both')
)

# Possible JnJ Competitive Levels + Social Only
COMP_LEVEL_CHOICES = (
    ('SOCIAL', 'Social Only'),
    ('NEWCOMER', 'Newcomer'),
    ('NOVICE', 'Novice'),
    ('INTERMEDIATE', 'Intermediate'),
    ('ADVANCED', 'Advanced'),
    ('ALLSTAR', 'All-Star')
)

# Years Dancing
MONTHS = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10  # 10+
YEARS_DANCING_CHOICES = (
    (MONTHS, '< 1'),
    (ONE, '1'),
    (TWO, '2'),
    (THREE, '3'),
    (FOUR, '4'),
    (FIVE, '5'),
    (SIX, '6'),
    (SEVEN, '7'),
    (EIGHT, '8'),
    (NINE, '9'),
    (TEN, '10+')
)

OTHER_DANCES = (
    ('AMERICAN SLOW WALTZ', 'American Slow Waltz'),
    ('ARGENTINE TANGO', 'Argentine Tango'),
    ('BALBOA', 'Balboa'),
    ('BLUES', 'Blues'),
    ('BOLERO', 'Bolero'),
    ('CAROLINA SHAG', 'Carolina Shag'),
    ('CHA CHA', 'Cha Cha'),
    ('CHARLESTON', 'Charleston'),
    ('COLLEGIATE SHAG', 'Collegiate Shag'),
    ('COUNTRY TWO STEP', 'Country Two Step'),
    ('EAST COAST SWING', 'East Coast Swing'),
    ('FOXTROT', 'Foxtrot'),
    ('HUSTLE', 'Hustle'),
    ('JIVE', 'Jive'),
    ('KIZOMBA', 'Kizomba'),
    ('LINDY HOP', 'Lindy Hop'),
    ('MAMBO', 'Mambo'),
    ('MERENGUE', 'Merengue'),
    ('NIGHTCLUB TWO STEP', 'Nightclub Two Step'),
    ('QUICKSTEP', 'Quickstep'),
    ('RUMBA', 'Rumba'),
    ('SAMBA', 'Samba'),
    ('SALSA', 'Salsa'),
    ('TANGO', 'Tango'),
    ('TRIPLE TWO STEP', 'Triple Two Step'),
    ('VIENNESE WALTZ', 'Viennese Waltz'),
    ('ZOUK', 'Zouk'),
    ('OTHER', 'Other')
)


class Dancer(models.Model):
    primary_dance_role = models.CharField(
        max_length=6,
        choices=PRIMARY_DANCE_ROLE_CHOICES,
        default='LEAD')
    competitive_level = models.CharField(
        max_length=12,
        choices=COMP_LEVEL_CHOICES,
        default='SOCIAL'
    )
    years_dancing = models.IntegerField(choices=YEARS_DANCING_CHOICES,
                                        default=MONTHS)
    age = models.PositiveIntegerField(validators=[MinValueValidator(6)])
    dj = models.BooleanField()
    teacher = models.BooleanField(default=False)
    other_dances = models.BooleanField()
    other_dance_styles = MultiSelectField(choices=OTHER_DANCES, blank=True, null=True)
    region = CountryField()
    song = models.ManyToManyField(Song, blank=True)

    def __unicode__(self):
        return '{0} {1}, aged {2} from {3}'.format(self.competitive_level, self.primary_dance_role,
                                                   self.age, self.region.name)

    def __str__(self):
        return '{0} {1}, aged {2} from {3}'.format(self.competitive_level, self.primary_dance_role,
                                                   self.age, self.region.name)

