import requests
import logging

class GooglePlacesAPI:
    BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

    def __init__(self, api_key):
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def _make_request(self, url, params):
        """
        Make a request to the Google Places API.

        :param url: The API endpoint URL.
        :param params: The parameters for the API request.
        :return: The JSON response from the API.
        """
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error in Google API request '{url}': {e}")
            raise  # Re-raise the exception for higher-level handling

    def search_restaurants(self, city_name):
        """
        Search for restaurants in the specified city using the Google Places API.

        :param city_name: The name of the city.
        :return: A list of restaurant details.
        """
        params = {
            'query': f'restaurants in {city_name}',
            'key': self.api_key,
        }

        response_json = self._make_request(self.BASE_URL, params)
        results = response_json.get('results', [])

        restaurants = []
        for result in results:
            place_id = result.get('place_id')
            restaurant_details = self.get_place_details(place_id)
            restaurants.append(restaurant_details)

        return restaurants

    def get_place_details(self, place_id):
        """
        Get details for a specific place using the Google Places API.

        :param place_id: The ID of the place.
        :return: Details of the place.
        """
        params = {
            'place_id': place_id,
            'key': self.api_key,
        }
        response_json = self._make_request(self.DETAILS_URL, params)
        details = response_json.get('result', {})

        # Extract relevant details from the response
        restaurant_details = {
            'name': details.get('name', ''),
            'address': details.get('formatted_address', ''),
            'rating': details.get('rating', ''),
            'menu': details.get('website', ''),  # Assuming menu is under the 'website' field
        }
        return restaurant_details
