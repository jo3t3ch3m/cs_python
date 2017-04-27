"""
Getting the computer to make a simple decision based on temperature readings
Objectives:
    To understand simple, two-way, and multi-way decision programming patterns.
    To understand the concept of Boolean expressions and the bool data type.
"""

# a program to convert celsius to fahrenheit

def main():
    celsius = eval(raw_input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is "+ str(fahrenheit)+ " degrees fahrenheit.")
# added str() and replaced commas with addition operators to omit unecessary output.

    if fahrenheit > 90:
        print("It's really hot in there. Be careful!")
    if fahrenheit < 30:
        print("Brrrr. Be sure to layer up!")
main()


