from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SearchQuery, SearchQueryCounter


@receiver(post_save, sender=SearchQuery)
def update_search_query_counter(sender, instance, created, **kwargs):
    if created:
        search_query = instance.search_query
        search_query_counter, created = SearchQueryCounter.objects.get_or_create(
            search_query=search_query
        )
        search_query_counter.counter += 1
        search_query_counter.save()
