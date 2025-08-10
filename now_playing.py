from spotify_auth import sp
from song_data import get_current_queue

def save_queue_as_playlist(playlist_name="Captured Queue"):
    """Capture the current playback queue and save as a new playlist"""
    user_id = sp.current_user()["id"]

    # Get songs from current queue
    tracks = get_current_queue()

    if not tracks:
        print("No songs found in the queue.")
        return

    # Create new playlist
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    playlist_id = playlist["id"]

    # Add songs to playlist
    track_uris = [track["uri"] for track in tracks]
    sp.playlist_add_items(playlist_id, track_uris)

    print(f"✅ Playlist '{playlist_name}' created with {len(track_uris)} tracks.")
