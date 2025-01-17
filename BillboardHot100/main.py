# Add billboard top 100 song from your chosen date.

from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# BASE_URL="https://www.billboard.com/charts/hot-100/"
# date_of_songs=input("Type Date in this format: YYYY-MM-DD: ")
# response = requests.get(BASE_URL+date_of_songs+"/")
# contents=response.text
# soup= BeautifulSoup(contents, 'html.parser')
# songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
# for song in songs:
#     print(song.getText().strip())

# Spotify Authentication
SPOTIPY_CLIENT_ID = 'smt'
SPOTIPY_CLIENT_SECRET = "smt"

# Authenticate Spotify 
sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        # Scope determines what can be viewed.
        scope = "playlist-modify-private",
        # scope = "user-top-read",
        # The URI Spotify uses after authenticating the user.
        redirect_uri = "https://example.com/",
        client_id = SPOTIPY_CLIENT_ID,
        client_secret = SPOTIPY_CLIENT_SECRET,
        show_dialog = True,
        # Saves the authentication token for reuse.
        cache_path = "token.txt",
        # username = 'LIN',
    )
)

# User Id
user_id = sp.current_user()["id"]
user_name = sp.current_user()["display_name"]

# Web Scrap Initialization
# Top 100 Billboard search based on dates
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

# Search URL based on song names
song_URL = []
year = date.split("-")[0]
for songNames in song_names:
    res = sp.search(q = f"track:{songNames} year:{year}", type = "track")
    print(res)
    try:
        URL = res["tracks"]["items"][0]["uri"]
        song_URL.append(URL)
    except IndexError:
        print(f"{songNames} cannot be found in Spotify")
print(song_URL)

# Playlist Creation
Playlist = sp.user_playlist_create(user = user_id, name = f"{date} Billboard 100", public = False, description = "Songs based on given date: " + date)
print(Playlist)
# Add songs to the list
sp.playlist_add_items(playlist_id = Playlist['id'], items = song_URL)


# try:
#     # Get the current user's information
#     user_info = sp.current_user()
#     user_id = user_info["id"]
#     user_name = user_info["display_name"]
#     print(f"Logged in as {user_name} (User ID: {user_id})")
#
#     # Create a new playlist
#     playlist_name = f"{date} Billboard 100"
#     playlist_description = f"Songs based on the Billboard Hot 100 chart for {date}"
#     private_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)
#     print(f"Playlist '{playlist_name}' created successfully.")
#
#     # Add songs to the playlist
#     playListSongs = sp.playlist_add_items(playlist_id=private_playlist["id"], items=song_names)
#     print("Songs added to the playlist successfully.")
#     print(playListSongs)
# except Exception as e:
#     print("An error occurred:", e)





