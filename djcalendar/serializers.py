from rest_framework import serializers
from .models import DjCalendar


class DjCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjCalendar
        fields = ('title', 'start', 'end', 'url')
