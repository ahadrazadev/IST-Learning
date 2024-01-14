# every_function.py

# Think of something you could store in a list and use each function introduced in this chapter at least once.
# For example, a list of countries:

countries = ["USA", "Canada", "France", "Japan", "Australia"]

# Append an item to the list
countries.append("Brazil")

# Insert an item at a specific index
countries.insert(2, "Germany")

# Remove an item by value
countries.remove("France")

# Pop an item by index
popped_country = countries.pop(1)

# Sort the list alphabetically
countries.sort()

# Reverse the order of the list
countries.reverse()

# Find the index of an item
index_of_japan = countries.index("Japan")

# Print the list
print("List of countries:", countries)
