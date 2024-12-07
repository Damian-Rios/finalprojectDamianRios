from django.db import models

class UserSet(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # Use the set ID from the API
    name = models.CharField(max_length=255)  # Set name, e.g., "Sword & Shield"
    series = models.CharField(max_length=255)  # Set series, e.g., "Sword & Shield"
    printed_total = models.IntegerField(null=True, blank=True)  # Number of cards in the set as printed
    total = models.IntegerField(null=True, blank=True)  # Total cards in the set including secret rares
    ptcgo_code = models.CharField(max_length=10, null=True, blank=True)  # Online play code, e.g., "SSH"
    is_completed = models.BooleanField(default=False)
    image_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
