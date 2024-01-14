# my_pizzas_your_pizzas.py

my_favorite_pizzas = ["Margherita", "Pepperoni", "Vegetarian"]
friend_pizzas = my_favorite_pizzas[:]

# Add a new pizza to the original list
my_favorite_pizzas.append("Hawaiian")

# Add a different pizza to the list friend_pizzas
friend_pizzas.append("BBQ Chicken")

# Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in my_favorite_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
