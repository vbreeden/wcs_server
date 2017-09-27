from django.db import models
from django.core.validators import MinValueValidator


class DanceOnTime(models.Model):
    dance_name = models.CharField(max_length=64)
    time_signature = models.CharField(max_length=5)
    tempo = models.PositiveIntegerField(validators=[MinValueValidator(50)])
    ticks_mp3 = models.CharField(max_length=128)
    vocals_mp3 = models.CharField(max_length=128)
