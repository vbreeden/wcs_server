from django.contrib import admin

from .models.bio import Bio
from .models.myths import Myth
from .models.research import Research

admin.site.register(Bio)
admin.site.register(Myth)
admin.site.register(Research)
