from django.db import models


class Myth(models.Model):
    title = models.CharField(max_length=128)
    topic = models.TextField()
