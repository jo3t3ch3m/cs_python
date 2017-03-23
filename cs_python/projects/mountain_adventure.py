# Choose your own adventure game
# WIZARD MOUNTAIN

# To be run in Python 2.7
# Change the functions, raw_input(), to input(), if you run in Python 3 or higher

# a text-based choose your own adventure game
# This adventure is like an upside down tree with branches
# this program is full of blocks of code, known as branches, or code branches

# Make sure to visit every branch to make sure all of the code works

def parachute_fail():
        print("\nyour parachute fails! Good luck!")

def wizard_mtn():
        print("\nYou land on the mountain, known as WIZARD MOUNTAIN")
        
def water():
        print("\nYou make a rough landing in the water! You put on your floaties and wait for rescue.")
        
def curl():
        print("Good thinking! Your plane crashes.")
        print("You are unconscious, but safe.")
        print("You are; however, in an unknown area with a lonely tree next to you.")
        choice = raw_input("\nA) Wake up, or B) Keep sleeping ")
        if choice == 'A':
                print("\nYou wake up, somewhere between the time of sunrise and noon.")
                print("You notice your plane and its parts are more than halfway beneath the ground!")
                print("You try to stand up...")
                choice = raw_input("Type, huh? ")
                if choice == 'huh?':
                        print("You are not standing up.")
                        print("You are actually stuck, halfway beneath some sand.")
                        print("You see a tree limb branching from the lonely tree that looks to be in reach.")
                        choice = raw_input("Do you reach for the branch? or Do you look around some more?" + " Type REACH or LOOK. ")
                        if choice == 'REACH':
                                print("You are able to pull yourself out of the sand!")
                                print("But, your journey is just beginning...")

                        elif answer2 == 'LOOK':
                                print("\nOops! You hesitated. You find that you are in quicksand and you should have reached for the branch!")
                                print(
        """
         _____       ___       ___  ___   _____  
        /  ___|     /   |     /   |/   | |  ___| 
        | |        / /| |    / /|   /| | | |__   
        | |  _    / ___ |   / / |__/ | | |  __|  
        | |_| |  / /  | |  / /       | | | |___  
        \_____/ /_/   |_| /_/        |_| |_____|
         
         _____   _     _   _____   _____   
        /  _  \ | |   / / |  ___| |  _  \  
        | | | | | |  / /  | |__   | |_| |  
        | | | | | | / /   |  __|  |  _  /  
        | |_| | | |/ /    | |___  | | \ \  
        \_____/ |___/     |_____| |_|  \_\
        """
     )
                        else:
                                print("Sorry, I can't understand you. ")
                                raw_input("\n\nPress the enter key to exit and run the program again!")
        if choice == 'B':
                print("You never wake from your slumber ")
                print(
        """
         _____       ___       ___  ___   _____  
        /  ___|     /   |     /   |/   | |  ___| 
        | |        / /| |    / /|   /| | | |__   
        | |  _    / ___ |   / / |__/ | | |  __|  
        | |_| |  / /  | |  / /       | | | |___  
        \_____/ /_/   |_| /_/        |_| |_____|
         
         _____   _     _   _____   _____   
        /  _  \ | |   / / |  ___| |  _  \  
        | | | | | |  / /  | |__   | |_| |  
        | | | | | | / /   |  __|  |  _  /  
        | |_| | | |/ /    | |___  | | \ \  
        \_____/ |___/     |_____| |_|  \_\
        """
     )
                raw_input("\n\nPress the enter key to exit and import the file name to run the program again!")
        
def valley():
        print("\nYou safely land in the middle of the goat herd.")
        
def goat_ride():
        print("\nThe trusty goat takes you to the nearest town. You are safe!")
        
def goat_herder():
        print("\nYou become a successful goat herder and make millions.")
        
def bad_wizard():
        print("\nThe object captures you and throws you into a magical stew paired with frog legs and magic chicken wings")
        
def good_wizard():
        print("\nA magical wizard comes from the object with a coconut and healing potion for you.")
        print("in a booming voice, the magical wizard explains, " + "Welcome to Wizard Mountain!!! " + " I suggest you explore this magical monstrousity!")
        
def answer_ab():
        print("Please type 'A' or 'B'")
        
def demise():
        print("You end your tumble at the end of the slope.")
        print("You have reached your breaking point.")
        raw_input("\n\npress the enter key to exit.")
        
def jagged_rock():
        print("""you manage to suddenly stop your flight by clutching the jagged rock.

You realize your hands and arms are super slimey.

but... why?

You spot an opening in the ground next to the rock.

The hole is just big enough for you to crawl through""")
        
def spikey_tree():
        print("You barely hang on to a spikey tree")
        print("\nOUCH! The tree is too spikey. You must let go of your grip and you continue your tumultuous tumble down the treacherous slope")
        print("You end up in a...")
        raw_input("\n\npress the enter key to exit.")

def hole():
        print("\nyou crawl through the hole")
        print("After a few minutes of shuffling down the hole, you plumet and land with a splash into an underground lake.")
        
        
        
def snail_demise():
        print("Draco spits out an acidic goo that covers you")
        print("You are unable to move and are stuck on this rock, hearing Draco's tales of his snail trails, until the end of your days")
        print(
        """
         _____       ___       ___  ___   _____  
        /  ___|     /   |     /   |/   | |  ___| 
        | |        / /| |    / /|   /| | | |__   
        | |  _    / ___ |   / / |__/ | | |  __|  
        | |_| |  / /  | |  / /       | | | |___  
        \_____/ /_/   |_| /_/        |_| |_____|
         
         _____   _     _   _____   _____   
        /  _  \ | |   / / |  ___| |  _  \  
        | | | | | |  / /  | |__   | |_| |  
        | | | | | | / /   |  __|  |  _  /  
        | |_| | | |/ /    | |___  | | \ \  
        \_____/ |___/     |_____| |_|  \_\
        """
     )
        raw_input("\n\npress the enter key to exit.")
        
        
        
print("""
You take your trusty propellar plane out for a joy ride.

Suddenly, the plane's propeller stops working and you are hurtling towards the ground!

You quickly spot a parachute next to you.

What do you do?
"""
)

print("\n**HINT** When making decisions, please type your answer as an uppercase letter.")

choice = raw_input("\nA) Quickly put on the parachute, B) Try to steer the plane towards the nearest body of water, or C) Curl up into a ball ")

# First branch of story
if choice == "A":
        print("\nYou jump out of the plane! You pull the string to open up the parachute. To your right, you see a mansion on top of a mysterious mountain. To your left, you see a goat herd in the valley. What do you do? ")
        choice = raw_input("A) Steer right or B) Steer left ")
        if choice == "A":
                wizard_mtn()
                print("You see an object in the distance.")
                choice = raw_input("\nA) Go to object? or B) Hike towards the mansion ")
                
                if choice == "A":
                        print("\nYou are weary from the excitement and your health is low from the landing.")
                        good_wizard()
                        choice = raw_input("\nExplore WIZARD MOUNTAIN? 'Y' or 'N' ")
                        if choice == 'Y':
                                print("You begin your exploration of Wizard Mountain.")
                                print("You are a little dizzy and sick from your landing.")
                                print("You spot a bottle of opened motion-sickness meds curiously lying on a rock to your left.")
                                choice = raw_input("ingest the contents of the motion-sickness bottle? 'Y' or 'N' ")
                                if choice == 'Y':
                                        print("Bad move? Yes!")
                                        print("The contents of the bottle was not what it said it was!")
                                        print("You begin to feel even more woozy and disoriented.")
                                        print("You see a light at the corner of your eye and a fuzzy dark figure appear to your left.")
                                        choice = raw_input("A) Go towards the light, or B) Ask the fuzzy dark figure for help ")
                                        if choice == 'A':
                                                print("You head towards the light")
                                                print("Uh Oh, the light source was the horizon of a steep hill!")
                                                choice = raw_input("You begin tumbling towards certain death.. Is this your demise? 'Y' or 'N' ")
                                                
                                                if choice == 'Y':
                                                        demise()
                                                        
                                                elif choice =='N':
                                                        print("""
You are a fighter!
Though, your ungraceful tumble down the steep slope past spikey trees and jagged rocks promises certain death
""")
                                                        choice = raw_input("A) Grab hold of a passing spikey tree, or B) Clutch a jagged rock? ")
                                                        
                                                        if choice == 'A':
                                                                spikey_tree()
                                                                demise()
                                                        elif choice == 'B':
                                                                jagged_rock()
                                                                choice = raw_input("A) Take a closer look at the rock, or B) Travel down the hole ")
                                                                if choice == 'A':
                                                                        print("""
Gross!

The rock is full of slimey snails!

You hear a tiny voice coming from one of these slimey snails

"""
                                                                              )
                                                                        choice = raw_input("Listen to the talkative snail? 'Y' or 'N' ")
                                                                        if choice == 'Y':
                                                                                print("The snail tells you tales of wonder about WIZARD MOUNTAIN")
                                                                                print("This is a place of treasure far as the eye can see, good wizards, bad wizards, and a terrible silicon breathing dragon")
                                                                                print("The snail tells you its name, 'Draco' ")
                                                                                print("Draco: What is your name?")
                                                                                name = raw_input()
                                                                                print("Draco: " + name + " You seem a bit battered, to say the least ")
                                                                                print("So, " + name)
                                                                                choice = raw_input(" Do you need my help? 'Y' or 'N' ")
                                                                                if choice == 'Y':
                                                                                        print("Draco: Next to this rock is a hole. I suggest you head down it")
                                                                                        print("You will find the reason of your life's journey starting there.")
                                                                                        hole()
                                                                                elif choice == 'N':
                                                                                        snail_demise()
                                                                                        
                                                                        
                                                                elif choice == 'B':
                                                                        hole()
                                                                
                                        
                                        elif choice == 'B':
                                                bad_wizard()
                                                        
                                                
                        
                        
                else:
                        bad_wizard()
                        
                
        elif choice == "B":
                valley()
                choice = raw_input("A) Ride a goat to the nearest town or B) Become a goat herder")
                if choice == "A":
                        goat_ride()
                
                elif choice == "B":
                        goat_herder()
                
        else:
                parachute_fail()        
                
elif choice == "B":
        # Second branch of the story
        water()
        
elif choice == "C":
        # Third branch of the story
        curl()
        
        
        

        
                
