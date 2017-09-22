from django.db import models

# Create your models here.
from django.db import models


class DjCalendar(models.Model):
    title = models.CharField(max_length=128)
    start = models.CharField(max_length=128)
    end = models.CharField(max_length=128)
    url = models.CharField(max_length=256)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.start[:10])
