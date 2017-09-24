from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    features = models.TextField()
    groove_url = models.TextField()
