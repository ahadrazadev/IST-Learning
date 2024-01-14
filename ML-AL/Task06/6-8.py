pets = [
    {'name': 'Buddy', 'kind': 'Dog', 'owner': 'Alice'},
    {'name': 'Whiskers', 'kind': 'Cat', 'owner': 'Bob'},
    {'name': 'Rex', 'kind': 'Dog', 'owner': 'Charlie'}
]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()
