from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.whatiswcs, name='whatiswcs'),
    url(r'^$', views.SongAndDancerViewSet, name='song-and-dancer'),
]
