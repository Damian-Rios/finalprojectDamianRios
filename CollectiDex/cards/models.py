from django.db import models

class UserCard(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cards')
    card_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    set = models.ForeignKey('sets.UserSet', on_delete=models.CASCADE, related_name='cards')
    set_number = models.CharField(max_length=20)
    rarity = models.CharField(max_length=100, null=True, blank=True)
    types = models.JSONField(null=True, blank=True)  # Requires PostgreSQL or JSON-capable DB
    market_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_small_url = models.URLField(max_length=500, null=True, blank=True)
    image_large_url = models.URLField(max_length=500, null=True, blank=True)
    tcgplayer_url = models.URLField(max_length=500, null=True, blank=True)

    quantity = models.PositiveIntegerField(default=1)  # Duplicates tracking

    def __str__(self):
        return f"{self.name} ({self.card_id})"
