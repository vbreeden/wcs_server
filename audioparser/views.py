from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from rest_framework.response import Response


def audioparser(request):
    template = loader.get_template('audioparser/audioparser.html')
    context = {
        '': []
    }
    return HttpResponse(template.render(context, request))
