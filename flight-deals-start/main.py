#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import notification_manager
import flight_data
import flight_search

data_Manger = DataManager()
SHEET_DATA = data_Manger.priceData
print(SHEET_DATA)