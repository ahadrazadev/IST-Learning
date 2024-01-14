person1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}
person2 = {'first_name': 'Alice', 'last_name': 'Smith', 'age': 25, 'city': 'London'}
person3 = {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'city': 'Paris'}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()
