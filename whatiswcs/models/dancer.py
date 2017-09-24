from django.db import models
from django_countries.fields import CountryField

# Dancers may primarily lead, follow, or regularly dance both roles
PRIMARY_DANCE_ROLE_CHOICES = (
    ('lead', 'LEAD'),
    ('follow', 'FOLLOW'),
    ('both', 'BOTH')
)

# Possible JnJ Competitive Levels + Social Only
COMP_LEVEL_CHOICES = (
    ('social only', 'SOCIAL'),
    ('newcomer', 'NEWCOMER'),
    ('novice', 'NOVICE'),
    ('intermediate', 'INTERMEDIATE'),
    ('advanced', 'ADVANCED'),
    ('allstar', 'ALLSTAR')
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
    ('MONTHS', '< 1'),
    ('ONE', '1'),
    ('TWO', '2'),
    ('THREE', '3'),
    ('FOUR', '4'),
    ('FIVE', '5'),
    ('SIX', '6'),
    ('SEVEN', '7'),
    ('EIGHT', '8'),
    ('NINE', '9'),
    ('TEN', '10+')
)


class Dancer(models.Model):
    primary_dance_role = models.CharField(
        max_length=6,
        choices=PRIMARY_DANCE_ROLE_CHOICES,
        default='lead')
    competitive_level = models.CharField(
        max_length=12,
        choices=COMP_LEVEL_CHOICES,
        default='social only'
    )
    years_dancing = models.IntegerField(choices=YEARS_DANCING_CHOICES,
                                        default=MONTHS)
    age = models.IntegerField()
    dj = models.BooleanField()
    other_dances = models.BooleanField()
    region = CountryField()


class OtherDances(models.Model):
    """This will house the other dances that a dancer may with to report.
    Currently on the list:
        American Slow Waltz
        Bolero
        Cha Cha
        Country Two Step
        East Coast Swing
        Foxtrot
        Hustle
        Jive
        Kizomba
        Mambo
        Merengue
        Nightclub Two Step
        Quickstep
        Rumba
        Salsa
        Tango
        Viennese Waltz
        Zouk
    """
    name = models.CharField(max_length=64)

    """This created the one-dancer-to-many-dances relationship we need.
    """
    dancer = models.ForeignKey(Dancer)

    """ I do not claim to know all of the possible partner dances so this field
    will capture any other dances a dancer may with to report.
    """
    other = models.TextField()

