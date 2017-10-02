from django.db import models


class Bio(models.Model):
    title = models.CharField(max_length=128)
    bio = models.TextField()
