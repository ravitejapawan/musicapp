from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('playlist/<int:playlist_id>/', home, name='home_with_playlist'),
]

