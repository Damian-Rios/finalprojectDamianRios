from django.shortcuts import render
from cards.models import UserCard
from sets.models import UserSet
from pokemontcgsdk import Card
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


def collection(request):
    user_cards = UserCard.objects.filter(user=request.user)
    return render(request, 'portfolio/total_cards_in_collection.html', {'user_cards': user_cards})


def get_market_price(card_id, variant_type):
    # Define a cache key for the card and variant type
    cache_key = f"card_{card_id}_variant_{variant_type}_price"

    # Try to get the price from the cache
    cached_price = cache.get(cache_key)
    if cached_price:
        return cached_price  # If cached, return the cached price

    # If not in cache, fetch the price from the API
    try:
        card_info = Card.find(card_id)
        if not card_info or not hasattr(card_info, 'tcgplayer') or not card_info.tcgplayer.prices:
            return 0  # If no data, return 0

        price_info = getattr(card_info.tcgplayer.prices, variant_type, None)
        market_price = price_info.market if price_info else 0

        # Cache the price for future requests, with a shorter expiry time (e.g., 15 minutes)
        cache.set(cache_key, market_price, timeout=15 * 60)  # Cache for 15 minutes

        return market_price
    except Exception as e:
        print(f"Error fetching market price: {e}")
        return 0  # Return 0 in case of an error


@login_required
def dashboard(request):
    user = request.user

    # Fetch user sets and cards
    user_cards = UserCard.objects.filter(user=user).select_related('card')  # Optimized query for UserCard data

    # Count the number of completed sets based on the is_completed field
    completed_sets = UserSet.objects.filter(is_completed=True).count()

    # Calculate statistics
    total_cards = sum(card.quantity for card in user_cards)
    total_value = 0
    for user_card in user_cards:
        card = user_card.card
        variant_type = user_card.variant_type

        market_price = get_market_price(card.card_id, variant_type) or 0
        total_value += market_price * user_card.quantity

    unique_cards = user_cards.values('card__card_id', 'variant_type').distinct().count()

    # Render the dashboard with stats and completed sets
    return render(request, 'portfolio/dashboard.html', {
        'total_cards': total_cards,
        'total_value': total_value,
        'unique_cards': unique_cards,
        'completed_sets': completed_sets,
        'user': user,
    })

