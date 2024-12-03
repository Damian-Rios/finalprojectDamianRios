from django.shortcuts import render
from cards.models import UserCard
from sets.models import UserSet
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    # Get the total number of cards in the collection
    total_cards = UserCard.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0

    # Get the total value of the collection (assumed to be fetched from card prices)
    total_value = UserCard.objects.filter(user=request.user).annotate(
        value=Sum('quantity')  # Just a placeholder. In actual use, multiply by price of each card
    ).aggregate(Sum('value'))['value__sum'] or 0

    # Get the number of unique cards in the collection
    unique_cards = UserCard.objects.filter(user=request.user).values('card_id').distinct().count()

    # Get the number of sets completed (you could define a set as "completed" when it has all cards)
    sets_completed = UserSet.objects.filter(user=request.user, is_completed=True).count()

    # Render the dashboard with the stats
    return render(request, 'dashboard.html', {
        'total_cards': total_cards,
        'total_value': total_value,
        'unique_cards': unique_cards,
        'sets_completed': sets_completed,
    })
