from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .models import Song, Dancer
from .serializers import SongSerializer, DancerSerializer
from .forms import SongForm, DancerForm


def whatiswcs(request):
    song = SongForm()
    dancer = DancerForm()
    context = {
        'song': song,
        'dancer': dancer
    }
    return render(request, 'whatiswcs/whatiswcs.html', context=context)


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()


class DancerViewSet(viewsets.ModelViewSet):
    serializer_class = DancerSerializer
    queryset = Dancer.objects.all()
