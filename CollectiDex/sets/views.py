from django.shortcuts import render
from pokemontcgsdk import Set
from .forms import SetFilterForm

def set_list(request):
    """ Display all Pokémon sets by default (with pagination) """
    page = int(request.GET.get('page', 1))  # Default to page 1
    page_size = 20  # Number of sets per page
    sets = Set.where(page=page, pageSize=page_size)  # Fetch paginated results
    return render(request, 'sets/set_list.html', {'sets': sets, 'page': page})

def search_sets(request):
    form = SetFilterForm(request.GET)
    sets = []
    page_size = 20
    page = int(request.GET.get('page', 1))

    if form.is_valid():
        # Get form data
        series = form.cleaned_data['series']
        set_id = form.cleaned_data['set_id']
        name = form.cleaned_data['name']

        # Build the query dynamically
        query_parts = []

        if series:
            series_query = ' OR '.join([f'series:"{s}"' for s in series])
            query_parts.append(f'({series_query})')
        if set_id:
            query_parts.append(f'id:"{set_id}"')
        if name:
            query_parts.append(f'name:"{name}*"')

        # Combine all query parts into the final query string
        query_string = " ".join(query_parts)

        # Fetch sets with the dynamic query
        queryTest = Set.where(q=query_string, page=page, pageSize=page_size)
        sets = queryTest

    return render(request, 'sets/search_results.html', {'form': form, 'sets': sets, 'page': page, 'page_size': page_size})
