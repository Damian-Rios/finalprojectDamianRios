from django.shortcuts import render
from cards.models import UserCard
from sets.models import UserSet
from cards.views import card_prices
from pokemontcgsdk import Card
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
import requests


# Helper function to check if all cards in a set are in the user's collection
def check_set_completion(user, user_set):
    # Get all card IDs in the set
    set_card_ids = user_set.cards.values_list('card_id', flat=True)

    # Check if the user owns each card in the set
    user_cards = UserCard.objects.filter(
        user=user,
        card__card_id__in=set_card_ids  # Matching the card_id from the CardModel
    ).values_list('card__card_id', flat=True)  # Get card_ids from the CardModel

    # If the user has all the cards in the set, return True
    return set_card_ids.count() == user_cards.count()


# Helper function to get market price of a card
# Helper function to get market price of a card
def get_market_price(card_id, variant_type):
    try:
        # Fetch the card info using the SDK
        card_info = Card.find(card_id)
        print(card_info.name)
        if not card_info or not hasattr(card_info, 'tcgplayer') or not card_info.tcgplayer.prices:
            print(f"No price data found for card: {card_id}, variant: {variant_type}")
            return 0  # Default to 0 if no price info is available

        # Access the price information for the given variant type
        price_info = getattr(card_info.tcgplayer.prices, variant_type, None)
        if price_info and hasattr(price_info, 'market'):
            print(price_info.market)
            return price_info.market  # Return the market price
        else:
            print(f"No market price found for variant: {variant_type}")
            return 0  # Default to 0 if market price is missing
    except Exception as e:
        print(f"Error fetching market price for {card_id}, variant: {variant_type}: {e}")
        return 0  # Default to 0 if an error occurs


@login_required
def dashboard(request):
    user = request.user
    sets = UserSet.objects.all().prefetch_related('cards')  # Optimized query to fetch all sets with related cards
    user_cards = UserCard.objects.filter(user=user).select_related('card')  # Optimized query for UserCard data

    completed_sets = []
    for user_set in sets:
        if check_set_completion(user, user_set):
            completed_sets.append(user_set)

    # Get the total number of cards in the collection
    total_cards = sum(card.quantity for card in user_cards)

    # Get the total value of the collection (multiplying quantity by market price)
    total_value = 0
    for user_card in user_cards:
        card = user_card.card  # Access the related Card instance
        variant_type = user_card.variant_type  # The variant type from UserCard
        market_price = get_market_price(card.card_id, variant_type) or 0  # Ensure market_price is not None
        total_value += user_card.quantity * market_price

    # Get the number of unique cards in the collection
    unique_cards = user_cards.values('card__card_id', 'variant_type').distinct().count()

    # Render the dashboard with the stats
    return render(request, 'portfolio/dashboard.html', {
        'total_cards': total_cards,
        'total_value': total_value,
        'unique_cards': unique_cards,
        'completed_sets': completed_sets,
        'user': user,
    })
