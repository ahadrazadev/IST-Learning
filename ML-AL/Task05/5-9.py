# no_users.py

# Add an if test to make sure the list of users is not empty.
usernames = []

if usernames:
    for username in usernames:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
