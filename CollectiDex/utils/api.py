import requests
from django.conf import settings

def fetch_pokemon_cards():
    url = f"{settings.POKEMON_TCG_API_BASE_URL}/cards"
    headers = {
        "X-Api-Key": settings.POKEMON_TCG_API_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()       # Return the JSON data if successful
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None
