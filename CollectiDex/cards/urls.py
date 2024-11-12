from django.urls import path
from . import views

urlpatterns = [
    path('pokemon-cards/', views.pokemon_card_list, name='pokemon_card_list'),
]
