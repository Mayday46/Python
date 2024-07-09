import requests
from pprint import pprint
from Credentials import SHEETY_FLIGHT_INFO_URL


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    priceData = None
    URL = SHEETY_FLIGHT_INFO_URL
    response = requests.get(url = URL)
    if response.status_code == 200:
        data = response.json()
        # print(data['prices'])
        # print(data)
        # pprint(data)
        # pprint(data['prices'])
        priceData = data['prices']
    else:
        print(f"Failed to fetch data: {response.status_code}")
