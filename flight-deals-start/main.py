#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
import notification_manager
import flight_data
import flight_search

data_Manger = DataManager()
SHEET_DATA = data_Manger.fetch_data()
# print(len(SHEET_DATA)) # -> 9
pprint(SHEET_DATA)
print()

# Testing assignment to iataCode
for eachItem in SHEET_DATA:
    data_Manger.update_iata_code(data = SHEET_DATA, iata_code = 'TESTING')

for each in range(2, len(SHEET_DATA) + 2):
    data_Manger.sheety_put(iata_Code = "TESTING" , rowCode= each)

print()
pprint(SHEET_DATA)
print()
