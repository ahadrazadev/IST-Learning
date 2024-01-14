# checking_usernames.py

# Create a program that simulates how websites ensure that everyone has a unique username.
current_users = ['john', 'eric', 'alice', 'bob', 'admin']
new_users = ['john', 'jane', 'alice', 'mike', 'anna']

# Loop through new_users to check if each new username has already been used.
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"Great! {new_user} is available.")
