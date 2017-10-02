from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import SongAndDancer
from .serializers import SongAndDancerSerializer
from .forms import SongAndDancerForm


def whatiswcs(request):
    song_and_dancer = SongAndDancerForm()
    context = {
        'songAndDancer': song_and_dancer,
    }
    return render(request, 'whatiswcs/whatiswcs.html', context=context)


def thankyou(request):
    context = {'': ''}
    return render(request, 'whatiswcs/thankyou.html', context=context)


class SongAndDancerViewSet(viewsets.ModelViewSet):
    serializer_class = SongAndDancerSerializer
    queryset = SongAndDancer.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        view = thankyou(request)
        return view
