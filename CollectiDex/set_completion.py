import os
import django

# Set the DJANGO_SETTINGS_MODULE before anything else
os.environ['DJANGO_SETTINGS_MODULE'] = 'CollectiDex.settings'

# Initialize Django settings
django.setup()

# Import the required models
from django.contrib.auth.models import User  # Import User model
from pokemontcgsdk import RestClient, Set, Card
from cards.models import UserCard, CardModel
from sets.models import UserSet
from django.db.models import Q

# Configure the API key
RestClient.configure('f89e3fab-3136-4936-971b-c171d0f4782d')  # Replace with your API key

def get_user_cards_for_set(user, set_id):
    # Query all UserCards associated with the user and the set
    user_cards = UserCard.objects.filter(user=user, card__set__id=set_id)

    # Collect the card ids of the user's owned cards for the set
    return [user_card.card.card_id for user_card in user_cards]

def check_set_completion(user, set_id):
    # Fetch the set from the database
    user_set = UserSet.objects.get(id=set_id)

    # Fetch all the cards for the set from the Pokémon API
    set_cards = Card.where(q=f'set.id:{set_id}')
    set_card_ids = {card.id for card in set_cards}

    # Fetch the user's cards for this set
    user_cards = get_user_cards_for_set(user, set_id)

    # Convert the user's card ids to a set for easier comparison
    owned_cards_in_set = set(user_cards)

    # Find the missing cards by subtracting the owned cards from the set cards
    missing_cards = set_card_ids - owned_cards_in_set

    # Check if there are any missing cards
    if not missing_cards:
        print(f"User has all cards in the {user_set.name} set. The set is complete.")
        user_set.is_completed = True
        user_set.save()
    else:
        print(f"Missing cards in {user_set.name} set: {missing_cards}")
        user_set.is_completed = False
        user_set.save()

    print()

# Example usage (assuming you have a user instance)
try:
    user = User.objects.get(username='testAdmin')  # Replace with the actual user
    user_sets = UserSet.objects.all()  # You can replace this with a filtered query for specific sets

    for user_set in user_sets:
        check_set_completion(user, user_set.id)
except User.DoesNotExist:
    print("User with the specified username does not exist.")
