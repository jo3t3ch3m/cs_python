output = 'output'

speechlet = {
    'outputSpeech': {
        'type': 'SSML',
        'ssml': output
        },
    'card': {
        'type': 'Simple',
        'title': 'JoeDaddy',
        'content': 'This is the introduction to the skill'
        },
    }

for card, card_info in speechlet.items():
    print("\nCard: " + card)
    content_title = card_info['content'] + " " + card_info['title']

    print("\tThe Card's content and title: " + content_title.title())
