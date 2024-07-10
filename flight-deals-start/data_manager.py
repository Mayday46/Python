import requests
from pprint import pprint
from Credentials import SHEETY_FLIGHT_INFO_URL
from Credentials import SHEETY_FLIGHT_GOOGLE_SPREADSHEETS

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def fetch_data(self): # This function returns all the flight offer.
        response = requests.get(url = SHEETY_FLIGHT_INFO_URL)
        data = response.json()
        return data['prices']

    def update_iata_code(self, data, iata_code):
        for item in data:
            # Check if the iataCode is empty, if it is modify...
            if item['iataCode'] == "":
                item['iataCode'] = iata_code
            else:
                continue
                

    def get_data(self, data):
        return data
    
    def sheety_put(self, iata_Code, rowCode):
        URL = SHEETY_FLIGHT_GOOGLE_SPREADSHEETS.replace("[Object ID]", str(rowCode))
        body = {
            "price": {
                "iataCode": iata_Code
            }
        }
        response = requests.put(url = URL, json=body)
