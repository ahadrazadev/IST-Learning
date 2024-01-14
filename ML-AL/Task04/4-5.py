# summing_a_million.py

# Make a list of the numbers from one to one million
numbers = list(range(1, 1000001))

# Use min() and max() to make sure the list starts at one and ends at one million
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

# Use sum() to see how quickly Python can add a million numbers
print("Sum:", sum(numbers))
