# seeing_the_world.py

places_to_visit = ["Tokyo", "Paris", "New York", "Sydney", "Rio de Janeiro"]

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted()
print("Alphabetical order:", sorted(places_to_visit))

# Show that the list is still in its original order
print("Original order:", places_to_visit)

# Print the list in reverse alphabetical order using sorted()
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that the list is still in its original order
print("Original order:", places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Change the order back to the original using reverse()
places_to_visit.reverse()
print("Original order:", places_to_visit)

# Change the order of the list using sort()
places_to_visit.sort()
print("Sorted order:", places_to_visit)

# Change the order of the list to reverse alphabetical using sort()
places_to_visit.sort(reverse=True)
print("Reverse sorted order:", places_to_visit)
