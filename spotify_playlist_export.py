import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ---------- CONFIG ----------
CLIENT_ID = "0133b16db4964b9b8a7e4c7b67951ecd"
CLIENT_SECRET = "d43d419411ce4c2aa4e525d034f8c515"
REDIRECT_URI = "http://127.0.0.1:8080"

SCOPE = "user-read-playback-state playlist-modify-public playlist-modify-private"

# ---------- AUTHENTICATION ----------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# ---------- FUNCTION TO GET CURRENT QUEUE ----------
def get_current_queue():
    try:
        queue_data = sp.queue()
        tracks = queue_data['queue']
        return tracks
    except Exception as e:
        print("Error getting queue:", e)
        return []

# ---------- FUNCTION TO CREATE PLAYLIST ----------
def create_playlist(name):
    user_id = sp.me()["id"]
    playlist = sp.user_playlist_create(user=user_id, name=name, public=False)
    return playlist["id"]

# ---------- FUNCTION TO ADD SONGS ----------
def add_songs_to_playlist(playlist_id, track_ids):
    sp.playlist_add_items(playlist_id, track_ids)

# ---------- MAIN SCRIPT ----------
if __name__ == "__main__":
    print("Fetching your Spotify queue...")
    queue_tracks = get_current_queue()

    if not queue_tracks:
        print("No songs in queue.")
        exit()

    playlist_name = input("Enter a name for the playlist: ")
    playlist_id = create_playlist(playlist_name)

    track_ids = [track["uri"] for track in queue_tracks]
    add_songs_to_playlist(playlist_id, track_ids)

    print(f"✅ Playlist '{playlist_name}' created successfully with {len(track_ids)} songs!")
