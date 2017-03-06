print("\nHere is a list of my favorite games")

games = [
    'tetris',
    'pong',
    'red rover']

def all_games():
    print("\nHere is a list of the games so far: ")
    print(games)

# a flag is a variable that acts as a signal to the program
# As long as the flag is True, the program will keep running
active = True
while active:
    new_game = raw_input("Please tell me your favorite game: ")

    if new_game == 'quit':
        print("\nYou've entered 'quit'")
        print("Come back again soon!")
        active = False

    else:
        games.append(new_game)
        print("\nHere is the updated list containing your game...")
        print(games)



    
