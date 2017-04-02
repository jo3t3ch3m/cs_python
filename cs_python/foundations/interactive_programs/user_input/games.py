print("\nHere is a list of my favorite games")

games = [
    'tetris',
    'pong',
    'red rover']

def all_games():
    print("\nHere is a list of the games so far: ")
    print(games)


new_game = ""
while new_game != 'quit':
    new_game = raw_input("Please tell me your favorite game: ")

    if new_game != 'quit':
        games.append(new_game)
        print("\nHere is the updated list containing your game...")
        print(games)

    else:
        print("\nYou've entered 'quit'")
        print("Come back again soon!")
        break

    
