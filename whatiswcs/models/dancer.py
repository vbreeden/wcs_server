from django.db import models
from django_countries.fields import CountryField

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
    ('ALLSTAR', 'Allstar')
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
        default='LEAD')
    competitive_level = models.CharField(
        max_length=12,
        choices=COMP_LEVEL_CHOICES,
        default='SOCIAL'
    )
    years_dancing = models.IntegerField(choices=YEARS_DANCING_CHOICES,
                                        default=MONTHS)
    age = models.IntegerField()
    dj = models.BooleanField()
    teacher = models.BooleanField(default=False)
    other_dances = models.BooleanField()
    region = CountryField()


class OtherDance(models.Model):
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
        Samba
        Salsa
        Tango
        Viennese Waltz
        Zouk
        Other
    """
    name = models.CharField(max_length=64)

    """This created the one-dancer-to-many-dances relationship we need.
    """
    dancer = models.ForeignKey(Dancer, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

