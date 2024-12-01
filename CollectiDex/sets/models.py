from django.db import models

class UserSet(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # Use the set ID from the API
    name = models.CharField(max_length=255)  # Set name, e.g., "Sword & Shield"
    series = models.CharField(max_length=255)  # Set series, e.g., "Sword & Shield"
    printed_total = models.IntegerField(null=True, blank=True)  # Number of cards in the set as printed
    total = models.IntegerField(null=True, blank=True)  # Total cards in the set including secret rares
    ptcgo_code = models.CharField(max_length=10, null=True, blank=True)  # Online play code, e.g., "SSH"
    release_date = models.DateField(null=True, blank=True)  # Release date of the set
    updated_at = models.DateTimeField(null=True, blank=True)  # Timestamp of the last update from the API
    symbol_url = models.URLField(max_length=500, null=True, blank=True)  # URL to set symbol image
    logo_url = models.URLField(max_length=500, null=True, blank=True)  # URL to set logo image

    def __str__(self):
        return self.name
