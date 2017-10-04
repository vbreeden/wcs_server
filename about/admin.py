from django.contrib import admin

from .models.bio import Bio
from .models.research import Research

admin.site.register(Bio)
admin.site.register(Research)
