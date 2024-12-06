from pokemontcgsdk import RestClient, Set, Card

# Configure the API key
RestClient.configure('f89e3fab-3136-4936-971b-c171d0f4782d')  # Replace with your API key

user_cards = ['sv1-1', 'sv1-2', 'sv1-3', 'sv1-4',
              'mcd19-1', 'mcd19-2', 'mcd19-3', 'mcd19-4', 'mcd19-5', 'mcd19-6', 'mcd19-7', 'mcd19-8', 'mcd19-9', 'mcd19-10', 'mcd19-11', 'mcd19-12']

user_sets = ['sv1', 'mcd19']

for user_set in user_sets:
    set_total = Set.find(f'{user_set}')
    print(f'Set: {set_total.name} Total: {set_total.total}')

print()

for user_card in user_cards:
    card_total = Card.find(f'{user_card}')
    print(f'Card: {card_total.name}, Set Total: {card_total.set.total}')















def set_total(user):
    # Get the user set
    user_set = UserSet.objects.get(name="Scarlet & Violet")
    total_cards = user_set.total  # Total cards in the set (without accounting for variants)

    # Get UserCard objects for the user, filter by set and user, then distinct by card_id
    user_cards = UserCard.objects.filter(
        card__set=user_set,  # The CardModel's set ForeignKey
        user=user              # The UserCard's user ForeignKey
    ).values('card_id').distinct()

    unique_cards_owned = user_cards.count()

    if unique_cards_owned == total_cards:
        print(f"{user.username} has completed the set {user_set.name}!")

        user_set.is_completed = True
        user_set.save()
    else:
        print(f"{user.username} has collected {unique_cards_owned}/{total_cards} cards in the set {user_set.name}.")

user = User.objects.get(username="testAdmin")  # Replace with a valid username
set_total(user)