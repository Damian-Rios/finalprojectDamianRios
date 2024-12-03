from django.contrib import admin
from .models import UserCard, Card

admin.site.register(Card)
admin.site.register(UserCard)

