from django.db import models
from django.contrib.auth.models import User

# Card model to store basic information about each card
class Card(models.Model):
    card_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    rarity = models.CharField(max_length=100, null=True, blank=True)
    types = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.card_id})"


# UserCard model to track each user's collection, including the variant and quantity
class UserCard(models.Model):
    class VariantChoices(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        HOLOFOIL = 'holofoil', 'Holofoil'
        REVERSE_HOLOFOIL = 'reverse_holofoil', 'Reverse Holofoil'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    variant_type = models.CharField(max_length=50, choices=VariantChoices.choices)
    quantity = models.PositiveIntegerField(default=1)  # Number of this variant the user owns

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'card', 'variant_type'], name='unique_user_card_variant')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.card.name} ({self.variant_type})"
