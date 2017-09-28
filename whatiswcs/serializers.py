from rest_framework import serializers
from .models import SongAndDancer


class SongAndDancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongAndDancer
        fields = (
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
