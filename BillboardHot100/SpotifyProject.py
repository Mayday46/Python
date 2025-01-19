
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication
SPOTIPY_CLIENT_ID = 'smt'
SPOTIPY_CLIENT_SECRET = 'smt'

class SpotifyPlaylistCreator:

    def __init__(self, client_id, client_secret, redirect_uri, scope, cache_path):
        self.sp = spotipy.Spotify(
            auth_manager = SpotifyOAuth (
                client_id = client_id,
                client_secret = client_secret,
                redirect_uri = redirect_uri,
                scope = scope,
                cache_path = cache_path,
                show_dialog= True
            )
        )

        self.user_id = self.sp.current_user()["id"]
        self.user_name = self.sp.current_user()["display_name"]

    def create_playlist(self, playlist_name, description):
        return self.sp.user_playlist_create(
            user = self.user_id,
            name = playlist_name,
            public = False,
            description = description
        )
    
    def search_song(self, song_name, year):
        try:
            result = self.sp.search(q = f"track:{song_name} year:{year}", type = "track")
            return result["tracks"]["items"][0]["uri"]
        except (IndexError, KeyError):
            return f"{song_name} cannot be found in Spotify"
    
    def add_song_to_playlist(self, playlist_id, song_list):
        return self.sp.playlist_add_items(playlist_id, song_list)
