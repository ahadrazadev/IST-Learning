# changing_guest_list.py

guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# Print the guest who can't make it
unavailable_guest = guests.pop(1)
print(f"Unfortunately, {unavailable_guest} can't make it to dinner.")

# Replace the name with a new person
new_guest = "Isaac Newton"
guests.insert(1, new_guest)

# Print new invitation messages
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
