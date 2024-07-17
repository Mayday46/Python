import os
import requests
from dotenv import load_dotenv


Auth_Token = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ['AMADEUS_FLIGHT_API'],
        self._api_secret = os.environ['AMADEUS_FLIGHT_API_SECRET'],
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url = Auth_Token, headers = header, data = body, verify = False)
        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    
    def citySearch(self, city_name):
        
        print(f"Using this given token -> {self._token}")
        query = {

            # "countryCode": "US",
            # Keyword that should represents the start of a word in a city name
            "keyword": city_name,
            # Number of results user want to see in response
            "max": 2,
            # Resources to be included example: Airports.
            "include": "AIRPORTS"
        }

        headers = {"Authorization": f"Bearer {self._token}"}

        response = requests.get(
            url = IATA_ENDPOINT,
            headers = headers,
            params = query
        )

        return response.json()["data"][0]['iataCode']
