from django.contrib import admin
from .models import SearchQuery, SearchQueryCounter


class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'search_query', 'timestamp')


class SearchQueryCounterAdmin(admin.ModelAdmin):
    list_display = ('search_query', 'counter')


admin.site.register(SearchQuery, SearchQueryAdmin)
admin.site.register(SearchQueryCounter, SearchQueryCounterAdmin)
