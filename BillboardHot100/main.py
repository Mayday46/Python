from BillboardScraper import BillboardScraper
from BillboardToSpotify import BillboardToSpotify
from SpotifyPlaylistCreator import SpotifyPlaylistCreator
from key import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

# Configuration
SPOTIPY_CLIENT_ID_UNIQUE = SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET_UNIQUE = SPOTIPY_CLIENT_SECRET
REDIRECT_URI = "https://example.com/"
SCOPE = "playlist-modify-private"
CACHE_PATH = "token.txt"

if __name__ == "__main__":
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    billboard_scraper = BillboardScraper(date)
    spotify_client = SpotifyPlaylistCreator(
        client_id = SPOTIPY_CLIENT_ID_UNIQUE,
        client_secret = SPOTIPY_CLIENT_SECRET_UNIQUE,
        redirect_uri = REDIRECT_URI,
        scope = SCOPE,
        cache_path = CACHE_PATH,
    )
    app = BillboardToSpotify(spotify_client, billboard_scraper)
    app.create_playlist_from_billboard()



