# ordinal_numbers.py

# Store the numbers 1 through 9 in a list.
numbers = list(range(1, 10))

# Loop through the list and use an if-elif-else chain to print the proper ordinal ending for each number.
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
