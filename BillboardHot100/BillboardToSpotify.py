class BillboardToSpotify:

    def __init__(self, spotify_client, billboard_scraper):
        self.spotify_client = spotify_client
        self.billboard_scraper = billboard_scraper
    
    def create_playlist_from_billboard(self):
        songs = self.billboard_scraper.scrape_top_100_songs()
        year = self.billboard_scraper.date.split("-")[0]
    
        # song_uris = [self.spotify_client.search_song(song, year) for song in songs]
        song_uris = []
        for song in songs:
            uri = self.spotify_client.search_song(song, year)
            if uri:
                song_uris.append(uri)

        song_uris = [uri for uri in song_uris if uri is not None]

        # Create a playlist and add songs
        playlist = self.spotify_client.create_playlist(
            name = f"{self.billboard_scraper.date} Billboard 100",
            description = f"Songs based on Billboard Hot 100 for {self.billboard_scraper.date}"
        )
        self.spotify_client.add_song_to_playlist(playlist["id"], song_uris)
        print(f"Playlist '{playlist['name']}' created successfully.")