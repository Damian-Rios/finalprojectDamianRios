from pokemontcgsdk import RestClient, Set

# Configure the API key
RestClient.configure('f89e3fab-3136-4936-971b-c171d0f4782d')  # Replace with your API key

# Variables
series = []
name = ''
set_id = ''


all_sets = Set.all()
#print(f"Found {len(all_sets)} sets.")
#for set in all_sets:
    #print(f"Set: {set.name}, ID: {set.id}, Series: {set.series}")

# Build the query dynamically
query_parts = []

if series:
    series_query = ' OR '.join([f'series:"{series}"' for series in series])
    query_parts.append(f'({series_query})')
if set_id:
    query_parts.append(f'id:"{set_id}"')
if name:
    query_parts.append(f'name:"{name}"')

# Combine all query parts into the final query string
query_string = " ".join(query_parts)

# Use the query string in your API call
queryTest = Set.where(q=query_string)

print("Query:", query_string)

print(f"Found {len(queryTest)} sets.")
for set in queryTest:
    print(f"Set: {set.name}, Id: {set.id}, Series: {set.series}, Release Date: {set.releaseDate}, Total Cards: {set.total}")