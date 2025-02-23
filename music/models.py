from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='songs/')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, blank=True)  # Manual selection enabled

    def __str__(self):
        return self.name
