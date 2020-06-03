from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)


    def __str__(self):
        return self.artist + " " + self.title