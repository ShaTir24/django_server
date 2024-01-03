from django.db import models


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)

    # storing the url of logo image
    album_logo = models.CharField(max_length=250)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    file_type = models.CharField(max_length=20)
