"""wcs_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from djcalendar import views as djviews
from whatiswcs import views as wcviews

router = routers.DefaultRouter()
router.register(r'djcalendar', djviews.DjCalendarViewSet, base_name='djcalendar')
router.register(r'song-and-dancer', wcviews.SongAndDancerViewSet,
                base_name='song-and-dancer')

urlpatterns = [
    url(r'^', include('whatiswcs.urls')),  # The WhatIsWCS app should house the main landing page
    url(r'^whatiswcs/', include('whatiswcs.urls')),  # Just in case someoene tries to navigate here
    url(r'^djcalendar/', include('djcalendar.urls')),
    url(r'^danceontime/', include('danceontime.urls')),
    url(r'^audioparser/', include('audioparser.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
