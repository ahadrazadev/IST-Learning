# more_guests.py

guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# Print message about the bigger dinner table
print("Good news! We found a bigger dinner table.")

# Add new guests
guests.insert(0, "Isaac Newton")
guests.insert(2, "Galileo Galilei")
guests.append("Nikola Tesla")

# Print new invitation messages
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
