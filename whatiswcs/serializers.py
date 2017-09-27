from rest_framework import serializers
from .models import Song, Dancer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'features', 'groove_url')


class DancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dancer
        fields = (
            'primary_dance_role', 'competitive_level', 'years_dancing',
            'age', 'dj', 'teacher', 'other_dances', 'other_dance_styles',
            'region', 'song',
        )
