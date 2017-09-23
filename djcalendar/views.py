from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework.response import Response
from .models import DjCalendar
from .serializers import DjCalendarSerializer


# This hosts the template html view
def djcalendar(request):
    template = loader.get_template('djcalendar/djcalendar.html')
    context = {
        '': []
    }
    return HttpResponse(template.render(context, request))


class DjCalendarViewSet(viewsets.ViewSet):
    """
    API endpoint that allows the schedule to be viewed or edited.
    """
    def list(self, request):
        queryset = DjCalendar.objects.all()
        serializer_class = DjCalendarSerializer(queryset, many=True)
        return Response(serializer_class.data)
