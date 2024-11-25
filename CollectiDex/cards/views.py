from django.shortcuts import render
from pokemontcgsdk import Card


def card_list(request):
    """ Display all Pokémon cards by default (with pagination) """
    page = int(request.GET.get('page', 1))  # Default to page 1
    page_size = 20  # Number of cards per page
    cards = Card.where(page=page, pageSize=page_size)  # Fetch paginated results
    return render(request, 'cards/card_list.html', {'cards': cards, 'page': page})


def search_cards(request):
    """ Search Pokémon cards by name """
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))  # Handle pagination
    page_size = 20
    cards = Card.where(q=f"name:{query}", page=page, pageSize=page_size) if query else Card.where(page=page,
                                                                                                  pageSize=page_size)
    return render(request, 'cards/card_list.html', {'cards': cards, 'query': query, 'page': page})


def filter_cards(request):
    """ Filter Pokémon cards based on selected filters """
    types = request.GET.getlist('types', [])
    supertype = request.GET.get('supertype', '')
    rarity = request.GET.get('rarity', '')

    query_filters = []

    if types:
        query_filters.append(' OR '.join([f"types:{type_}" for type_ in types]))
    if supertype:
        query_filters.append(f"supertype:{supertype}")
    if rarity:
        query_filters.append(f"rarity:{rarity}")

    query = ' '.join(query_filters)

    page = int(request.GET.get('page', 1))  # Handle pagination
    page_size = 20
    cards = Card.where(q=query, page=page, pageSize=page_size) if query else Card.where(page=page, pageSize=page_size)

    return render(request, 'cards/card_list.html',
                  {'cards': cards, 'filters': types, 'supertype': supertype, 'rarity': rarity, 'page': page})
