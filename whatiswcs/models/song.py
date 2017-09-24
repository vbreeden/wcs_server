from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    features = models.TextField(blank=True, null=True)
    groove_url = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '{0} by {1}'.format(self.title, self.artist)

    def __str__(self):
        return '{0} by {1}'.format(self.title, self.artist)
