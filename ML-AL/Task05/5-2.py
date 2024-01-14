# more_conditional_tests.py

# Tests for equality and inequality with strings
fruit = 'apple'
print("\nIs fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit != 'orange'? I predict True.")
print(fruit != 'orange')

# Tests using the lower() function
city = 'New York'
print("\nIs city.lower() == 'new york'? I predict True.")
print(city.lower() == 'new york')

# Numerical tests
age = 25
print("\nIs age >= 21? I predict True.")
print(age >= 21)

print("\nIs age < 18? I predict False.")
print(age < 18)

# Tests using the and keyword and the or keyword
temperature = 28
print("\nIs temperature > 0 and temperature < 30? I predict True.")
print(temperature > 0 and temperature < 30)

print("\nIs temperature > 30 or temperature < 15? I predict True.")
print(temperature > 30 or temperature < 15)

# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)

# Test whether an item is not in a list
print("\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)
