from django.db import models

class UserCard(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cards')
    card_id = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    set = models.ForeignKey('sets.UserSet', on_delete=models.CASCADE, related_name='cards')
    set_number = models.CharField(max_length=20)
    rarity = models.CharField(max_length=100, null=True, blank=True)
    types = models.JSONField(null=True, blank=True)  # Requires PostgreSQL or JSON-capable DB
    quantity = models.PositiveIntegerField(default=0)  # Duplicates tracking
    market_price_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.card_id})"
