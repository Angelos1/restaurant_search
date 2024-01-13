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
        # start_time = time.time()

        city_name = request.POST.get('city_name', '')
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')

        # Save search query to the database
        SearchQuery.objects.create(ip_address=ip_address, search_query=city_name)


        # Make API request here

        # Add logic to fetch restaurant data from API based on city_name
        # Use GooglePlacesAPI to get restaurant data
        # start_time2 = time.time()

        google_api = GooglePlacesAPI(api_key=self.google_api_key)
        restaurants = google_api.search_restaurants(city_name)

        # end_time2 = time.time()
        # api_response_time2 = end_time2 - start_time2
        # print(f"API Response Time2: {api_response_time2} seconds")
        # print(f"Query: restaurants in {city_name}")
        # print("API Response:", restaurants)
        # end_time = time.time()
        # api_response_time = end_time - start_time
        # print(f"API Response Time: {api_response_time} seconds")
        return render(request, self.template_name, {'city_name': city_name, 'restaurants': restaurants})

