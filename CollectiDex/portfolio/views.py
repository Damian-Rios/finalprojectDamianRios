from django.shortcuts import render
from cards.models import UserCard
from sets.models import UserSet
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required


# Helper function to check if all cards in a set are in the user's collection
def check_set_completion(user, user_set):
    # Get all card IDs for the set (e.g., sv1-1, sv1-2, sv1-3...)
    set_card_ids = [f"{user_set.id}-{i}" for i in range(1, user_set.total + 1)]

    # Check if all cards exist in the user's collection
    user_cards = UserCard.objects.filter(
        user=user,
        card_id__in=set_card_ids
    ).values_list('card_id', flat=True)  # Get only the card_id of the user's collection

    # If the user has all the cards, the length of user_cards should match the length of set_card_ids
    return set_card_ids == sorted(user_cards)

@login_required
def dashboard(request):
    user = request.user
    sets = UserSet.objects.all()
    cards = UserCard.objects.filter(user=user).values_list('card_id', flat=True)

    completed_sets = []
    for user_set in sets:
        if check_set_completion(user, user_set):
            completed_sets.append(user_set)

    # Get the total number of cards in the collection
    total_cards = 0
    user_cards = UserCard.objects.filter(user=user)

    for card in user_cards:
        total_cards += card.quantity

    # Get the total value of the collection (assumed to be fetched from card prices)
    total_value = UserCard.objects.filter(user=request.user).annotate(
        value=Sum('quantity')  # Just a placeholder. In actual use, multiply by price of each card
    ).aggregate(Sum('value'))['value__sum'] or 0

    # Get the number of unique cards in the collection
    unique_cards = UserCard.objects.filter(user=request.user).values('card_id').distinct().count()

    # Render the dashboard with the stats
    return render(request, 'portfolio/dashboard.html', {
        'total_cards': total_cards,
        'total_value': total_value,
        'unique_cards': unique_cards,
        'completed_sets': completed_sets,
        'user': user,
    })
