import requests


class GooglePlacesAPI:
    BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

    def __init__(self, api_key):
        self.api_key = api_key

    def search_restaurants(self, city_name):
        params = {
            'query': f'restaurants in {city_name}',
            'key': self.api_key,
        }

        # url = f"{self.BASE_URL}?query={params['query']}&key={params['key']}"
        # print("API Request URL:", url)

        response = requests.get(self.BASE_URL, params=params)
        results = response.json().get('results', [])

        # print("API response:", response.json())
        # print("results:", len(results))
        restaurants = []
        for result in results:
            place_id = result.get('place_id')
            restaurant_details = self.get_place_details(place_id)
            restaurants.append(restaurant_details)

        # print(restaurants)
        return restaurants

    def get_place_details(self, place_id):
        params = {
            'place_id': place_id,
            'key': self.api_key,
        }
        response = requests.get(self.DETAILS_URL, params=params)
        details = response.json().get('result', {})

        # Extract relevant details, you may need to adapt this based on the actual structure of the response
        restaurant_details = {
            'name': details.get('name', ''),
            'address': details.get('formatted_address', ''),
            'rating': details.get('rating', ''),
            'menu': details.get('website', ''),  # Assume menu is under the 'website' field,
        }
        # print("details :", restaurant_details)
        return restaurant_details