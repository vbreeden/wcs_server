from django.http import HttpResponse


def danceontime(request):
    return HttpResponse("Hello, world. You're at the Dance On Time screen.")
