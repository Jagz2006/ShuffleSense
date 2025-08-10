
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials (replace with your own from Spotify Developer Dashboard)
CLIENT_ID = "0133b16db4964b9b8a7e4c7b67951ecd"
CLIENT_SECRET = "d43d419411ce4c2aa4e525d034f8c515"
REDIRECT_URI = "http://127.0.0.1:8080"

# Required scope for reading and creating playlists
SCOPE = "user-read-playback-state playlist-modify-public playlist-modify-private"

# Create Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))
