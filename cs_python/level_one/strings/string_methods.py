# Python 2.7

name = "ada lovelace"
print(name.title())

# Above we stored the value, "ada lovelace" in a variable named, 'name'
# The dot (.) after name in name.title() tells Python to make the title() method
# act on the variable, name.

# CONCATENATING STRINGS/COMBINING STRINGS

# While we program more and more, we'll find that it is useful for us to combine strings
# for example, let's say we wanted to combine to seperate variables,
# like first name and last name.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# or with a little more content and use of variables:
message = "Hello " + full_name.title() + "!"
print(message)

# Quiz start
score = 0
while True:
    # First Question
    print("\nWho was " + full_name.title() + "?")
    choice1 = raw_input("\nA) first woman to go to mars, or" +
                        "\nB) first computer programmer, or" +
                        "\nC) first president of U.S." +
                        "\n")
    if choice1 == 'B':
        print("\tCorrect!" +
              "\n\tOne point is added to your score!")
        score += 1
    elif choice1 == 'quit':
        break
    else:
        print("\tClose!" +
              "\n\tPlease try again...")

    # Second Question
    print("\nWhat MACHINE did " + full_name.title() + " program?")
    choice2 = raw_input("\nA) The washer machine, or" +
                        "\nB) A car, or" +
                        "\nC) The Babbage Machine" +
                        "\n")
    if choice2 == 'B':
        print("\tCorrect!" +
              "\n\tOne point is added to your score!")
        score += 1
    elif choice2 == 'quit':
        break
    else:
        print("\tClose!" +
              "\n\tPlease try again...")                
print "\nHere is your score: "
print score

