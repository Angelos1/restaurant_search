from django.shortcuts import render
from django.views import View
from .models import SearchQuery
from .google_places_api import GooglePlacesAPI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class SearchView(View):
    template_name = 'search_app/search.html'
    google_api_key = config.get('GOOGLE', 'api_key')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        city_name = request.POST.get('city_name', '')
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')

        # Save search query to the database
        SearchQuery.objects.create(ip_address=ip_address, search_query=city_name)

        # Make Google API request
        google_api = GooglePlacesAPI(api_key=self.google_api_key)
        restaurants = google_api.search_restaurants(city_name)

        return render(request, self.template_name, {'city_name': city_name, 'restaurants': restaurants})
