
from pokemontcgsdk import RestClient, Card, Set, Subtype, Supertype, Rarity, Type

# Configure the API key
RestClient.configure('f89e3fab-3136-4936-971b-c171d0f4782d')  # Replace with your API key

"""
types = Card.where(q='types:water')
print(f"Found {len(types)} types.")
for type in types:
    print(f"Type: {type.name}")


sets = Set.where(q='series:Base')
print(f"Found {len(sets)} sets.")
for set in sets:
    print(f"Set: {set.name}")

print()


allSets = Set.all()
print(f"Found {len(allSets)} sets.")
for set in allSets:
    print(f"Set: {set.name}, ID: {set.id}, Series: {set.series}")

print()

supertypesTest = Supertype.all()
print(f"Found {len(supertypesTest)} supertypes.")
print(supertypesTest)
print()

subtypesTest = Subtype.all()
print(f"Found {len(subtypesTest)} subtypes.")
print(subtypesTest)

print()

rarityTest = Rarity.all()
print(f"Found {len(rarityTest)} rarity.")
print(rarityTest)

print()
typesTest = Type.all()
print(f"Found {len(typesTest)} types.")
print(typesTest)
print()

setCards = Card.where(q='set.id:sv2 types:water')
print(f"Found {len(setCards)} cards.")
for card in setCards:
    print(f"Card: {card.name}, ID: {card.id}, Set: {card.set.name}, type: {card.types}")

print()
"""
# Variables
supertype = ''
subtypes = []
types = []
rarity = ''
series = ['scarlet & violet']
sets = []

# Build the query dynamically
query_parts = []

if supertype:
    query_parts.append(f'supertype:{supertype}')
if subtypes:
    subtypes_query = ' AND '.join([f'subtypes:"{subtype}"' for subtype in subtypes])
    query_parts.append(f'({subtypes_query})')
if types:
    types_query = ' OR '.join([f'types:"{type}"' for type in types])
    query_parts.append(f'({types_query})')
if rarity:
    query_parts.append(f'rarity:"{rarity}"')
if series:
    if "Other" in series:
        series_query = ' AND '.join([f'-set.series:"{series}"' for series in series])
        query_parts.append(f'({series_query})')
    else:
        series_query = ' OR '.join([f'set.series:"{series}"' for series in series])
        query_parts.append(f'({series_query})')

if sets:
    sets_query = ' OR '.join([f'set.id:"{set}"' for set in sets])
    query_parts.append(f'({sets_query})')

# Combine all query parts into the final query string
query_string = " ".join(query_parts)

# Use the query string in your API call
queryTest = Card.where(q=query_string, pageSize=250, page=12)

print("Query:", query_string)

print(f"Found {len(queryTest)} cards.")
for card in queryTest:
    #print(f"Card: {card.name}, Supertype: {card.supertype}, Subtype: {card.subtypes}, Rarity: {card.rarity}, Type: {card.types}, Series: {card.set.series}, Set: {card.set.name}")
    print(f" Set Name: {card.set.name}, ID: {card.set.id}")

queryTest = Card.where(q='set.name:"paradox rift"', pageSize=10, page=1)
for card in queryTest:
    #print(f"Card: {card.name}, Supertype: {card.supertype}, Subtype: {card.subtypes}, Rarity: {card.rarity}, Type: {card.types}, Series: {card.set.series}, Set: {card.set.name}")
    print(f" Set Name: {card.set.name}, ID: {card.set.id}")

#if __name__ == "__main__":
    #test_cards()

