from django.contrib import admin

from .models.song import Song
from .models.dancer import Dancer

admin.site.register(Song)
admin.site.register(Dancer)
