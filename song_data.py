from spotify_auth import sp

def get_current_queue():
    """Fetch the currently playing track and upcoming queue"""
    try:
        queue = sp.queue()
        tracks = []

        # Include currently playing track first
        if queue["currently_playing"]:
            tracks.append({
                "name": queue["currently_playing"]["name"],
                "uri": queue["currently_playing"]["uri"]
            })

        # Add queued tracks
        for track in queue["queue"]:
            tracks.append({
                "name": track["name"],
                "uri": track["uri"]
            })

        return tracks
    except Exception as e:
        print(f"Error fetching queue: {e}")
        return []
