
prompt = "\nTell me your favorite game and I'll add it to the list."
prompt += "\nEnter 'quit' to end the program"
prompt += "\nEnter game here: "

games = []

def all_games():
    print("\nHere is a list of the games so far: ")
    print(games)

while True:
    new_game = raw_input(prompt)

    if new_game == 'quit':
        break

    elif new_game != 'quit':
        games.append(new_game)
        all_games()
