# Using a while loop with lists
# Python 2.7
# Objective: move items from one list to another

# Consider a list of newly registered but unverified users of a website. After we
# verify these users, we need to move them to seperate list of confirmed users.

# From what we just learned, we can use a while loop to pull users
# from the list of unconfirmed users as we verify them and then add them to a
# seperate list of confirmed users.

# Create a new python file named, confirm_users.py

# Let's start with the users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['albert', 'ada', 'watson', 'crick']
confirmed_users = []

# We need to verify each user until there are no more unconfimed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# All confirmed users displayed
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
