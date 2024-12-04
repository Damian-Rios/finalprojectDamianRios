from django.contrib import admin
from .models import UserCard, CardModel

admin.site.register(CardModel)
admin.site.register(UserCard)

