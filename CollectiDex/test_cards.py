from pokemontcgsdk import RestClient, Card

# Configure the API key
RestClient.configure('f89e3fab-3136-4936-971b-c171d0f4782d')  # Replace with your API key


def test_cards():
    print("Starting test...")

    # Fetching cards with a specific query (cards from Generations set with supertype 'pokemon')
    try:
        cards = Card.where(q='set.name:generations supertype:pokemon')
        print(f"Found {len(cards)} cards.")

        for card in cards:
            print(f"Card: {card.name}, ID: {card.id}, Supertype: {card.supertype}")

    except Exception as e:
        print(f"Error occurred: {e}")

    print("Test completed.")


if __name__ == "__main__":
    test_cards()
