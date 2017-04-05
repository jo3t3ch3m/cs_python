import random
number = random.randint(1, 100) 

while True:
    guess = int(raw_input("Guess a number between 1-100: ")) 
    if guess == number:
            print("You guessed correctly!")
    elif guess > number:
            print("Your guess was too high")
    elif guess < number:
            print("Your guess was too low")
    else:
            print("Your did not enter a number")
