from django.shortcuts import render, redirect, get_object_or_404
from pokemontcgsdk import Card
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CardFilterForm
from .models import UserCard
from sets.models import UserSet  # Import the UserSet model
import requests
from django.contrib import messages


def card_prices(card):
    prices = []
    if hasattr(card, 'tcgplayer') and card.tcgplayer and hasattr(card.tcgplayer, 'prices') and card.tcgplayer.prices:
        price_data = card.tcgplayer.prices.__dict__
        for price_type, price_info in price_data.items():
            # Ensure price_info is not None and contains valid data
            if price_info:
                prices.append({
                    'type': price_type or 'N/A',
                    'low': getattr(price_info, 'low', 'N/A') or 'N/A',
                    'high': getattr(price_info, 'high', 'N/A') or 'N/A',
                    'market': getattr(price_info, 'market', 'N/A') or 'N/A',
                })
    return prices


def card_list(request):
    """ Display all Pokémon cards by default (with pagination) """
    page = int(request.GET.get('page', 1))  # Default to page 1
    page_size = 20  # Number of cards per page
    form = CardFilterForm(request.GET)

    if form.is_valid() and 'name' in form.cleaned_data and form.cleaned_data['name']:
        name = form.cleaned_data['name']
        cards = Card.where(q=f'name:"{name}*"', page=page, pageSize=page_size)
    else:
        cards = Card.where(page=page, pageSize=page_size)

    for card in cards:
        card.prices = card_prices(card)

    return render(request, 'cards/card_list.html', {'form': form, 'cards': cards, 'page': page, 'page_size': page_size})


def search_cards(request):
    form = CardFilterForm(request.GET)
    cards = []
    page_size = 20
    page = int(request.GET.get('page', 1))

    if form.is_valid():
        # Get form data
        supertype = form.cleaned_data['supertype']
        pokemon_subtypes = form.cleaned_data['pokemon_subtypes']
        trainer_subtypes = form.cleaned_data['trainer_subtypes']
        energy_subtypes = form.cleaned_data['energy_subtypes']
        all_subtypes = pokemon_subtypes + trainer_subtypes + energy_subtypes
        combine_subtypes = form.cleaned_data['combine_subtypes']
        types = form.cleaned_data['types']
        common_rarities = form.cleaned_data['common_rarities']
        other_rarities = form.cleaned_data['other_rarities']
        all_rarities = common_rarities + other_rarities
        name = form.cleaned_data['name']
        series = form.cleaned_data['series']
        sv_sets = form.cleaned_data['scarlet_violet_sets']

        # Build the query dynamically
        query_parts = []

        if supertype:
            query_parts.append(f'supertype:{supertype}')
        if all_subtypes:
            if combine_subtypes == 'and':
                subtypes_query = ' AND '.join([f'subtypes:"{subtype}"' for subtype in all_subtypes])
            else:
                subtypes_query = ' OR '.join([f'subtypes:"{subtype}"' for subtype in all_subtypes])
            query_parts.append(f'({subtypes_query})')
        if types:
            types_query = ' OR '.join([f'types:"{type}"' for type in types])
            query_parts.append(f'({types_query})')
        if series:
            if "other_series" in series:
                # Exclude the common series
                excluded_series = [
                    "scarlet & violet", "sword & shield", "sun & moon",
                    "xy", "black & white", "heartgold & soulsilver", "platinum",
                    "diamond & pearl", "ex", "base"
                ]
                excluded_query = " ".join([f'-set.series:"{s}"' for s in excluded_series])
                query_parts.append(f'({excluded_query})')
            else:
                # Include the selected series
                series_query = ' OR '.join([f'set.series:"{s}"' for s in series])
                query_parts.append(f'({series_query})')
        if all_rarities:
            query_parts.append(f'rarity:"{all_rarities}"')
        if name:
            query_parts.append(f'name:"{name}*"')
        if sv_sets:
            sv_sets_query = ' OR '.join([f'set.id:"{set}"' for set in sv_sets])
            query_parts.append(f'({sv_sets_query})')

        # Combine all query parts into the final query string
        query_string = " ".join(query_parts)

        # Call the API to fetch the cards
        query_test = Card.where(q=query_string, page=page, pageSize=page_size)
        cards = query_test

        for card in cards:
            card.prices = card_prices(card)

    return render(request, 'cards/card_list.html', {'form': form, 'cards': cards, 'page': page, 'page_size': page_size})


@login_required
def add_card_to_collection(request, card_id):
    """Add a card to the user's collection by fetching data from the API."""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided
        user = request.user
        try:
            card = Card.find(card_id)  # Fetch the card from the API
        except Exception:
            return render(request, 'cards/card_list.html', {'error': 'Card not found'})

        # Create or get the associated set
        set_data = card.set.__dict__
        user_set, created = UserSet.objects.get_or_create(
            id=set_data['id'],
            defaults={
                'name': set_data['name'],
                'series': set_data['series'],
                'printed_total': set_data.get('printedTotal'),
                'total': set_data.get('total'),
                'ptcgo_code': set_data.get('ptcgoCode'),
            }
        )

        # Combine card number with total number of cards in the set
        set_number = f"{card.number}/{card.set.total}" if card.number and card.set.total else "Unknown/Unknown"

        existing_card, created = UserCard.objects.get_or_create(
            user=user,
            card_id=card.id,
            defaults={
                'name': card.name,
                'series': card.set.series,
                'set': user_set,
                'set_number': set_number,
                'rarity': card.rarity,
                'types': card.types,
                'quantity': 0,  # Default to 0, will increment below
                'market_price_url': card.tcgplayer.url if hasattr(card, 'tcgplayer') and hasattr(card.tcgplayer, 'url') else '',
            }
        )

        # Increment quantity if the card already exists
        existing_card.quantity += quantity
        existing_card.save()

        if created:
            messages.success(request, f'{card.name} was successfully added to your collection!')
        else:
            messages.success(request, f'{card.name} quantity updated in your collection!')

        return redirect(f'{request.META.get("HTTP_REFERER", "/")}')
