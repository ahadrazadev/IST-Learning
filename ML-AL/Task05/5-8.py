# hello_admin.py

# Make a list of five or more usernames, including the name 'admin'.
usernames = ['admin', 'john', 'eric', 'alice', 'bob']

# Loop through the list and print a greeting to each user.
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
