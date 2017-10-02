from django.db import models


class Research(models.Model):
    title = models.CharField(max_length=128)
    topic = models.TextField()
