from django.shortcuts import render
from django.views import View
from .models import SearchQuery
from .google_places_api import GooglePlacesAPI
import configparser

# Read configuration from config.ini using configparser
config = configparser.ConfigParser()
config.read('config.ini')


class SearchView(View):
    # Template name for rendering the HTML page
    template_name = 'search_app/search.html'

    google_api_key = config.get('GOOGLE', 'api_key')

    def get(self, request):
        # Render the initial page when a GET request is received
        return render(request, self.template_name)

    def post(self, request):
        # Handle POST requests when the user submits the search form

        # Get the city_name from the submitted form data
        city_name = request.POST.get('city_name', '')

        # Get the user's IP address, defaulting to 'unknown' if not available
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')

        # Save search query to the database using the SearchQuery model
        SearchQuery.objects.create(ip_address=ip_address, search_query=city_name)

        # Make Google API request and retrieve a list of restaurants based on the city_name
        google_api = GooglePlacesAPI(api_key=self.google_api_key)
        try:
            restaurants = google_api.search_restaurants(city_name)
        except Exception as e:
            error_message = "Something went wrong, please contact the administrator - Error message: " + str(e)
            return render(request, self.template_name, {'error_message': error_message})

        # Render the HTML page with the returned search results
        return render(request, self.template_name, {'city_name': city_name, 'restaurants': restaurants})
