from django.shortcuts import render, get_object_or_404
from .models import Playlist

def home(request, playlist_id=None):
    playlists = Playlist.objects.all()
    selected_playlist = None
    songs = []
    
    if playlist_id:
        selected_playlist = get_object_or_404(Playlist, id=playlist_id)
        songs = selected_playlist.songs.all()
    
    return render(request, 'music/home.html', {
        'playlists': playlists,
        'selected_playlist': selected_playlist,
        'songs': songs
    })
