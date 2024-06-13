
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication
SPOTIPY_CLIENT_ID = 'smt'
SPOTIPY_CLIENT_SECRET = 'smt'

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "https://example.com/",
        client_id = SPOTIPY_CLIENT_ID,
        client_secret = SPOTIPY_CLIENT_SECRET,
        show_dialog = True,
        cache_path = "token.txt",
        username= 'LIN',
    )
)
user_id = sp.current_user()["id"]
