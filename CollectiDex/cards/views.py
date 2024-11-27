from django.shortcuts import render
from pokemontcgsdk import Card
from .forms import CardFilterForm

def card_list(request):
    """ Display all Pokémon cards by default (with pagination) """
    page = int(request.GET.get('page', 1))  # Default to page 1
    page_size = 20  # Number of cards per page
    cards = Card.where(page=page, pageSize=page_size)  # Fetch paginated results
    return render(request, 'cards/card_list.html', {'cards': cards, 'page': page, 'page_size': page_size})


def search_cards(request):
    form = CardFilterForm(request.GET)
    cards = []
    page_size = 250
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
        if all_rarities:
            query_parts.append(f'rarity:"{all_rarities}"')

        # Combine all query parts into the final query string
        query_string = " ".join(query_parts)

        # Call the API to fetch the cards (replace this with your actual API call)
        query_test = Card.where(q=query_string, page=page, pageSize=page_size)
        cards = query_test  # Assuming the API call returns a list of cards

    return render(request, 'cards/search_results.html', {'form': form, 'cards': cards, 'page': page, 'page_size': page_size})
