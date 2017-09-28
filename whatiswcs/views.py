from django.shortcuts import render
from rest_framework import viewsets
from .models import SongAndDancer
from .serializers import SongAndDancerSerializer
from .forms import SongAndDancerForm


def whatiswcs(request):
    song_and_dancer = SongAndDancerForm()
    context = {
        'songAndDancer': song_and_dancer,
    }
    return render(request, 'whatiswcs/whatiswcs.html', context=context)


class SongAndDancerViewSet(viewsets.ModelViewSet):
    serializer_class = SongAndDancerSerializer
    queryset = SongAndDancer.objects.all()
