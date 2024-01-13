from django.db import models


# Model representing individual search queries
class SearchQuery(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    search_query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.search_query} - {self.timestamp}"


# Model representing individual search queries with their number of times they were submitted
class SearchQueryCounter(models.Model):
    search_query = models.CharField(max_length=255, primary_key=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.search_query
