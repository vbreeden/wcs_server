from rest_framework import fields, serializers
from django_countries.serializers import CountryFieldMixin
from .models import SongAndDancer, OTHER_DANCES


class SongAndDancerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    other_dance_styles = fields.MultipleChoiceField(choices=OTHER_DANCES)

    class Meta:
        model = SongAndDancer
        fields = (
            'id',
            'title',
            'artist',
            'features',
            'song_url',
            'primary_dance_role',
            'competitive_level',
            'years_dancing',
            'age',
            'dj',
            'teacher',
            'other_dance_styles',
            'region',
        )
