from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import DjCalendar
from .serializers import DjCalendarSerializer


# This hosts the template html view
def djcalendar(request):
    return HttpResponse("Hello, world. You're at the DJ Calendar screen.")


class DjCalendarViewSet(viewsets.ViewSet):
    """
    API endpoint that allows the schedule to be viewed or edited.
    """
    def list(self, request):
        queryset = DjCalendar.objects.all()
        serializer_class = DjCalendarSerializer(queryset, many=True)
        return Response(serializer_class.data)
