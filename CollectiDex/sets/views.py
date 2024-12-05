from django.http import Http404
from django.shortcuts import render, get_object_or_404
from pokemontcgsdk import Set, Card
from .forms import SetFilterForm
from cards.views import card_variants, card_prices

def set_list(request):
    page = int(request.GET.get('page', 1))  # Default to page 1
    page_size = 20  # Number of cards per page
    form = SetFilterForm(request.GET)

    if form.is_valid() and 'name' in form.cleaned_data and form.cleaned_data['name']:
        name = form.cleaned_data['name']
        sets = Set.where(q=f'name:"{name}*"', page=page, pageSize=page_size, orderBy='-releaseDate')
    else:
        sets = Set.where(page=page, pageSize=page_size, orderBy='-releaseDate')

    return render(request, 'sets/set_list.html', {'form':form, 'sets': sets, 'page': page, 'page_size': page_size})


def set_view(request, set_id):
    page_size = 20
    page = int(request.GET.get('page', 1))

    set = Set.find(f'{set_id}')

    try:
        # Fetch all the cards for this set
        set_cards = Card.where(q=f'set.id:"{set_id}"', page=page, pageSize=page_size, orderBy='number')
    except Exception:
        set_cards = []


    for card in set_cards:
        card.prices = card_prices(card)
        card.variants = card_variants(card)

    return render(request, 'sets/set_view.html', {'set': set, 'set_cards': set_cards, 'page': page, 'page_size': page_size})

def search_sets(request):
    form = SetFilterForm(request.GET)
    sets = []
    page_size = 20
    page = int(request.GET.get('page', 1))

    if form.is_valid():
        # Get form data
        set_series = form.cleaned_data['series']
        set_name = form.cleaned_data['name']

        # Build the query dynamically
        query_parts = []

        if set_name:
            query_parts.append(f'name:"{set_name}*"')

        if set_series:
            if "other_series" in set_series:
                # Exclude common series
                excluded_series = [
                    "scarlet & violet", "sword & shield", "sun & moon",
                    "xy", "black & white", "heartgold & soulsilver", "platinum",
                    "diamond & pearl", "ex", "base"
                ]
                excluded_query = " ".join([f'-series:"{s}"' for s in excluded_series])
                query_parts.append(f'({excluded_query})')
            else:
                # Include selected series
                series_query = ' OR '.join([f'series:"{s}"' for s in set_series])
                query_parts.append(f'({series_query})')

        # Combine all query parts into the final query string
        query_string = " ".join(query_parts)

        # Call the API to fetch the sets
        query_test = Set.where(q=query_string, page=page, pageSize=page_size)
        sets = query_test

    return render(request, 'sets/set_list.html', {'form': form, 'sets': sets, 'page': page, 'page_size': page_size})
