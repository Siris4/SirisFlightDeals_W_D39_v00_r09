import os
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY', 'Custom Message / Key does not exist')



class FlightSearch:
    # this class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.city_name = None
        self.price = None

    def get_destination_code(self, city_name):
        self.city_name = city_name
        # self.price = price
        # GET request from Tequila API

        headers = {
            "apikey": TEQUILA_API_KEY
            }

        # city_name="City_name test: PRG"

        query_params = {
            "term":city_name,
            "locale":"en-US",
            "location_types":"airport",
            "limit":7,
            "active_only":"true",
        }
        # iata_code = flight_search.get_destination_code(row["city"])
        query_request_url = "https://api.tequila.kiwi.com/locations/query"      #  toss this: f"{TEQUILA_ENDPOINT}/locations/query"
        query_response = requests.get(url=query_request_url, headers=headers, params=query_params)

        query_response.raise_for_status()
        query_data = query_response.json()
        # print(f"The query_data is: {query_data}")

        for city_iteration in range(query_params['limit']):
            # global IATA_city_code
            IATA_city_code = query_data['locations'][city_iteration]['code']

            # return "TESTING" code for now, to ensure it's working. We can get Tequila API data later:
            dest_code = IATA_city_code   #entered into IATA Code column of that particular row's city name
            print(f"The city name is: {city_name}")
            print(dest_code)
            return dest_code

   ######################## END OF IATA CODE LOGIC ########################


    def get_price(self, price_and_city_params):
        # define the endpoint Price and City search URL:
        price_and_city_url = "https://api.tequila.kiwi.com/v2/search"

        # define the search/query parameters:
        # TODO: price_and_city_params taken to main.py

        # Include your API key in the headers
        price_and_city_headers = {
            "apikey": TEQUILA_API_KEY  # Replace YOUR_API_KEY_HERE with your actual Tequila API key
        }

        # Make the GET request
        price_and_city_response = requests.get(url=price_and_city_url, params=price_and_city_params, headers=price_and_city_headers)
        print(f"The price_and_city_response is: {price_and_city_response}")

        price_and_city_response.raise_for_status()
        price_and_city_data = price_and_city_response.json()
        print(f"The price_and_city_data is: {price_and_city_data}")

        # TODO: Print the City and Price for all the cities listed:

        if 'data' in price_and_city_data and price_and_city_data['data']:
            self.price = price_and_city_data['data'][0]['price']
            print(f"The cheapest flight price is: {self.price}")
            return self.price
        else:
            print("No flight data was found.")
            return None
