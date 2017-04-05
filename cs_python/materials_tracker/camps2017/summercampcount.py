# A simple program to show Tech Em Studios summer camp names
# and enrollment numbers

# Python 2.7

import time

summer_camps_2017 = {
    'minecraft camp (modding)': '3',
    'gaming (mobile or VR)': '2',
    'raspberry pi camp': '1',
    'alexa camp': '0',
    'minecraft camp jcc': '0',
    'minecraft (3D)': '5',
    'robot camp': '2',
    'you tube': '5',
    'gaming (3D and VR)': '2',
    'digital arts': '4',
    'mobile apps': '3',
    'game design jcc': '0',
    'ethical hacking': '4',
    'build your own laptop': '2',
    'intro to coding jcc': '0'
    }

camp_list = raw_input("For a list of upcoming summer camps offered by Tech Em, type 'show'")
if camp_list == 'show':
    for camp in summer_camps_2017:
        print("\t" + camp.title())
else:
    raw_input("\n\npress the enter key to exit.")
camp_numbers = raw_input("To show camp names and enrollment for each, type 'number'")
if camp_numbers == 'number':
    for camp, numbers in summer_camps_2017.items():
        print("\n" + camp.title() + "'s enrollment numbers are:")
        for number in numbers:
            print("\t" + number)
else:
    raw_input("\n\npress the enter key to exit.")

marketing = raw_input("\nIf you wish to increase enrollment numbers for each camp, type 'increase'")
if marketing == 'increase':
    print("\nYou will now be directed to an available marketing robot...")
    time.sleep(3)
    active = True
    while active:
        print("loading...")
        time.sleep(3)
        print "..."
        time.sleep(3)
        print("still loading...")
        time.sleep(1)
        print("psshhhhhhhkeerrrrr ding der ding der ding pshhhh")
        time.sleep(5)
        print("\nCongratulations!")
        print("\nYou are now being connected with...")
        time.sleep(2)
        print("\nMark, your neighborhood friendly marketing robot")
        time.sleep(1)
        print("\nPlease hold")
        active = False

else:
    raw_input("\n\npress the enter key to exit.")

    
        
    

    
    
