
favorite_languages = {
    'Alice': 'Python',
    'Bob': 'JavaScript',
    'Charlie': 'C++',
    'Diana': 'Java',
    'Edward': 'Python'
}

people_to_poll = ['Alice', 'Charlie', 'Eva']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person}, for responding!")
    else:
        print(f"Hey, {person}, we invite you to take the poll.")

