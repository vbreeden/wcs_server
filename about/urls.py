from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^research/', views.research, name='research'),
    url(r'^bio/', views.bio, name='bio'),
]
