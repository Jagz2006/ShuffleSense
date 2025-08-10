
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials (replace with your own from Spotify Developer Dashboard)
CLIENT_ID = "Client id"
CLIENT_SECRET = "Client secret"
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
