from django.contrib import admin
from .models import SearchQuery, SearchQueryCounter

# Customizing the admin interface for the SearchQuery model
class SearchQueryAdmin(admin.ModelAdmin):
    # Columns to be displayed in the admin list view
    list_display = ('ip_address', 'search_query', 'timestamp')

# Customizing the admin interface for the SearchQueryCounter model
class SearchQueryCounterAdmin(admin.ModelAdmin):
    list_display = ('search_query', 'counter')


admin.site.register(SearchQuery, SearchQueryAdmin)
admin.site.register(SearchQueryCounter, SearchQueryCounterAdmin)
