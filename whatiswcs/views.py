from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Song, Dancer
from .serializers import SongSerializer, DancerSerializer
from .forms import SongForm


def whatiswcs(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SongForm()
    return render(request, 'whatiswcs/whatiswcs.html', {'form': form})


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()


class DancerViewSet(viewsets.ModelViewSet):
    serializer_class = DancerSerializer
    queryset = Dancer.objects.all()
