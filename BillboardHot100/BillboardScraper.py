import requests
from bs4 import BeautifulSoup

class BillboardScraper:

    def __init__(self, date):
        self.date = date
        self.base_url = "https://www.billboard.com/charts/hot-100/"
        self.song_names = []
    

    def scrape_top_100_songs(self):
        response = requests.get(self.base_url + self.date)
        soup = BeautifulSoup(response.text, 'html.parser')
        song_names_spans = soup.select("li ul li h3") # This is the HTML format of where the song name is located on Billboard
        self.song_names = [song.getText().strip() for song in song_names_spans]
        return self.song_names
