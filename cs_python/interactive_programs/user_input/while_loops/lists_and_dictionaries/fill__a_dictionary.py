# Python 2.7

# Let's make a polling program which each pass through the loop prompts for
# the participant's name and response. We'll store the data we gather in a dictionary,
# because we want to connect each response with a particular user.

# In this example, the user's will be asked for their name and a stream or river they visited

# setting up empty dictionary
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = raw_input("\nWhat is your name? ")
    response = raw_input("Which VA stream did you take measurements? ")

    # storing the responses.
    responses[name] = response

    # Find out if there is another team member that needs to input data
    repeat = raw_input("Is there another person on your team that needs to respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# Polling is complete. Now, Show the results.
print("\n--- Stream Visitation Results ---")
for name, response in responses.items():
    print(name + " took measurements at the " + response + " site.")
    
