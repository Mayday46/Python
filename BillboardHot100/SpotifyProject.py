
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
