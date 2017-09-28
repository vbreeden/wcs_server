from django.db import models
from django.core.validators import MinValueValidator
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField


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


class SongAndDancer(models.Model):
    """
    After a great deal of deliberation I have decided that I'm looking for each
    participant to only provide one song. What I'm looking for is the songs that bubble
    to the very top of danceability, not a list of 'really good songs' from each person.
    """
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    features = models.TextField(blank=True, null=True)
    song_url = models.CharField(max_length=400, null=True)

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
    age = models.PositiveIntegerField(validators=[MinValueValidator(6)],
                                      default=18, blank=True, null=True)
    dj = models.BooleanField()
    teacher = models.BooleanField(default=False)
    region = CountryField(blank=True, null=True)
    other_dance_styles = MultiSelectField(choices=OTHER_DANCES, blank=True, null=True)

    def __unicode__(self):
        return '{0} by {1}'.format(self.title, self.artist)

    def __str__(self):
        return '{0} by {1}. Role: {2}. Level: {3}. Age: {4}'.format(self.title,
                                                                    self.artist,
                                                                    self.primary_dance_role,
                                                                    self.competitive_level,
                                                                    self.age)
