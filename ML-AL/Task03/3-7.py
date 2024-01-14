# shrinking_guest_list.py

guests = ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"]

# Print message about the limited space
print("Unfortunately, we can only invite two people for dinner.")

# Remove guests one at a time until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, we can't invite you to dinner.")

# Print invitations to the remaining guests
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Empty the list
del guests[:]
print("The guest list is now empty:", guests)
