from BillboardScraper import BillboardScraper
from BillboardToSpotify import BillboardToSpotify
from SpotifyPlaylistCreator import SpotifyPlaylistCreator
from key import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
from tkinter import Tk, Label, Entry, Button, messagebox

# Configuration
# SPOTIPY_CLIENT_ID_UNIQUE = SPOTIPY_CLIENT_ID
# SPOTIPY_CLIENT_SECRET_UNIQUE = SPOTIPY_CLIENT_SECRET
# REDIRECT_URI = "https://example.com/"
# SCOPE = "playlist-modify-private"
# CACHE_PATH = "token.txt"

# if __name__ == "__main__":
#     date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#     billboard_scraper = BillboardScraper(date)
#     spotify_client = SpotifyPlaylistCreator(
#         client_id = SPOTIPY_CLIENT_ID_UNIQUE,
#         client_secret = SPOTIPY_CLIENT_SECRET_UNIQUE,
#         redirect_uri = REDIRECT_URI,
#         scope = SCOPE,
#         cache_path = CACHE_PATH,
#     )
#     app = AppGUI(spotify_client, billboard_scraper)
#     app.run()

CONFIG = {
    "client_id": SPOTIPY_CLIENT_ID,
    "client_secret": SPOTIPY_CLIENT_SECRET,
    "redirect_uri": "https://example.com/",
    "scope": "playlist-modify-private",
    "cache_path": "token.txt"
}


class MainApp:

    def __init__(self):
        self.spotiy_client = SpotifyPlaylistCreator(**CONFIG)

        # Create the main window

        self.window = Tk()
        self.window.title("Billboard to Spotify")
        self.window.geometry("400x200")

        self.setup_ui()
    
    
    def setup_ui(self):
        # Setup UI components

        label = Label(self.window, text="Enter the date in this format YYYY-MM-DD:", font=("Arial", 12))
        label.pack(pady=10)

        self.date_entry = Entry(self.window, font=("Arial", 12))
        self.date_entry.pack(pady=10)

        submit_button = Button(
            self.window,
            text="Create Playlist",
            font=("Arial", 12),
            command=self.create_playlist
        )
        submit_button.pack(pady=10)
    
    def create_playlist(self):
        date = self.date_entry.get()
        try:
            scraper = BillboardScraper(date)
            billboard_to_spotify = BillboardToSpotify(self.spotiy_client, scraper)
            billboard_to_spotify.create_playlist_from_billboard()
            messagebox.showinfo("Success", "Playlist created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def run(self):
        # self.setup_ui()
        self.window.mainloop()
    

if __name__ == "__main__":
    app = MainApp()
    app.run()


