from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SearchQuery, SearchQueryCounter

# Define a signal receiver function to update SearchQueryCounter when a new SearchQuery is saved
@receiver(post_save, sender=SearchQuery)
def update_search_query_counter(sender, instance, created, **kwargs):
    # Check if the instance (SearchQuery) was just created
    if created:
        # Retrieve the search query from the newly created SearchQuery instance
        search_query = instance.search_query
        # Use get_or_create to retrieve an existing SearchQueryCounter or create a new one
        search_query_counter, created = SearchQueryCounter.objects.get_or_create(
            search_query=search_query
        )
        search_query_counter.counter += 1
        search_query_counter.save()
