# buffet.py

# A buffet-style restaurant offers only five basic foods.
foods = ("Pizza", "Burger", "Salad", "Pasta", "Sushi")

# Use a for loop to print each food the restaurant offers
for food in foods:
    print(food)

# Try to modify one of the items (will result in an error)
# foods[0] = "Fried Chicken"

# The restaurant changes its menu, replacing two items with different foods
foods = ("Fried Chicken", "Fish and Chips", "Salad", "Pasta", "Sushi")

# Use a for loop to print each of the items on the revised menu
for food in foods:
    print(food)
