from django.contrib import admin

from .models.song import Song
from .models.dancer import Dancer, SongList

admin.site.register(Song)
admin.site.register(Dancer)
admin.site.register(SongList)
