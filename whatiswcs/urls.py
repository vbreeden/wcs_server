from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.whatiswcs, name='whatiswcs'),
    url(r'^$', views.SongViewSet, name='songs'),
    url(r'^$', views.DancerViewSet, name='dancers'),
]
