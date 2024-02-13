#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from data_manager_W_D39_v00_r09 import DataManager
from flight_search_W_D39_v00_r09 import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()  # needs () because it is a Class
flight_search = FlightSearch()
sheet_data = data_manager.get_request_for_getting_destination_data()
origin_iata_code = "SAN"

# TODO: Authenticate with a Bearer Token
# TODO: Ensure all sensitive data is extracted and created into an Environment Variable, above here.


print("Sheet Data before any Updates: ")
pprint(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
# def iataCode_Checking():
for row in sheet_data:
    # global flight_search
    # check if "iatacode" for the row is empty:
    if row.get("iataCode") == "":
        print(f"iataCode data is empty for {row['city']}, UPDATING ROW...")
        # use the flightsearch class to get the corresponding iata code for the city:
        iata_code = flight_search.get_destination_code(row["city"])
        # update the "iatacode" in the row with the new value:
        row["iataCode"] = iata_code
        # iata_code = iata_code
        # return iata_code
        price_and_city_params = {
            "fly_from": "SAN",
            "fly_to": "FRA",
            "date_from": "02/13/2024",
            "date_to": "08/13/2024",
            "return_from": "04/04/2021",  # This seems to be a past date, double-check if it's correct
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_fly_duration": 20,
            "ret_from_diff_city": "true",
            "ret_to_diff_city": "true",
            "one_for_city": 0,
            "one_per_date": 0,
            "adults": 1,
            "children": 0,
            "infants": 0,
            "selected_cabins": "C",
            "mix_with_cabins": "M",
            "adult_hold_bag": "1,0",
            "adult_hand_bag": "1,1",
            "child_hold_bag": "0,0",
            "child_hand_bag": "0,0",
            "only_working_days": "false",
            "only_weekends": "false",
            "partner_market": "us",
            "price_from": 0,
            "price_to": 550,
            "max_stopovers": 2,
            "max_sector_stopovers": 2,
            "vehicle_type": "aircraft",
            "sort": "price",
            "limit": 1  # to get the top/cheapest flight of the whole bunch that were found in the search
        }

        flight_search.get_price(price_and_city_params)
    else:
        # if "iatacode" is not empty, print a message and skip to the next row:
        print(f"iataCode for {row['city']} is already set to {row['iataCode']}, Skipping this row...")

print("\nSheet Data After Updates: ")
pprint(sheet_data)

# update the google sheet via sheety api if any changes were made:
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# elif not sheet_data[0]["iataCode"] == "":
#     print()
#     print("Data was found inside the first row of the IATA Code Column")
# # iataCode_Checking()




