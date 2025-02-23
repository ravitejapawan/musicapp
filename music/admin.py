from django.contrib import admin
from .models import Song, Playlist

class PlaylistAdmin(admin.ModelAdmin):
    filter_horizontal = ('songs',)  # Makes song selection easier

admin.site.register(Song)
admin.site.register(Playlist, PlaylistAdmin)
