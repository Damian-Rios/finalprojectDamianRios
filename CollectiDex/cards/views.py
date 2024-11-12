from django.shortcuts import render
from utils.api import fetch_pokemon_cards  # Adjusted import path

def pokemon_card_list(request):
    cards_data = fetch_pokemon_cards()
    context = {"cards": cards_data.get("data", [])} if cards_data else {"cards": []}
    return render(request, "cards/card_list.html", context)
