# Featuring 2 or more ways to skin this cat

# Might be good idea to work on option two first.

# ONE:
# mimic changint the whole function that holds the dictionary.
# (again, or JSON? Let's hope it's a dictionary,
#       since that is what we know how to work with)
##def build_speechlet_repsonse(title, output, reprompt_text, should_end_session)
##
##    return {
##        'outputSpeech': {
##            'type': 'SSML',
##            'ssml': output
##            },
##    card = {
##        'type': 'Simple',
##        'title': 'JoeDaddy',
##        'content': 'This is a basic alexa skill and so forth'
##        }


# TWO:
# Just work with changing the whole model of the dictionary.
##card = {
##    'type': 'Simple',
##    'title': 'JoeDaddy',
##    'content': 'This is a basic alexa skill and so forth'
##    }
##
##print("Original card content is: ")
##print("\n")
##print(card['content'])
##
##user_says = raw_input("\tPlease type: bored" + "\n\tType your response here: ")
##
##if user_says == 'bored':
##    content = 'If you think your baby is uncomfortable due to gas, try the following'
##
##card['content'] = content
##
##print("The new card content is: ")
##print("\n")
##print(card['content'])

# TWO ver 2.0
# create an example function that houses the dictionary
# attempt to modify the dictionary's value outside of the function
##def example():
##    
##    card = {
##        'type': 'Simple',
##        'title': 'JoeDaddy',
##        'content': 'This is a basic alexa skill and so forth'
##        }
##
##print("Original card content is: ")
##print("\n")
##print(card['content'])
##
##
##user_says = raw_input("\tPlease type: bored" + "\n\tType your response here: ")
##
##if user_says == 'bored':
##    content = 'If you think your baby is uncomfortable due to gas, try the following'
##
##card['content'] = content
##
##print("The new card content is: ")
##print("\n")
##print(card['content'])

# In ver 2.0, card is unknown to Python, because it is 'hidden' inside the function

# TWO ver. 2.1
# Try modifying the dictionary value whilst inside the example function from 2.0

def example():
    
    card = {
        'type': 'Simple',
        'title': 'JoeDaddy',
        'content': 'This is a basic alexa skill and so forth'
        }

    print("Original card content is: ")
    print("\n")
    print(card['content'])


    user_says = raw_input("\tPlease type: bored" + "\n\tType your response here: ")

    if user_says == 'bored':
        content = 'If you think your baby is uncomfortable due to gas, try the following'

    card['content'] = content

    print("The new card content is: ")
    print("\n")
    print(card['content'])
# Call the function to test ver 2.1 to skin the cat
# Theoretically, this should work in the lamda function.
# The build_speechlet_response is already called in the babyCalmTechniques function
# when the skill is 'beckoned'.
example()
