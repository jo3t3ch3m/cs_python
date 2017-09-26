from graphics import *

def main():
    win = GraphWin("Celsius Converter", 400, 500)
    win.setCoords(0.0, 0.0, 3.0, 4.0)


    # Draw the Interface
    Text(Point(1, 3), " Celsius Converter: ").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)
    input = Entry(Point(2, 3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2, 1), "")
    output.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)


    # Listen for Mouse Click Event
    win.getMouse()


    # Convert the Input
    celsius = eval(input.getText())
    fahrenheit = 9.0/5.0 * celsius + 32


    if fahrenheit > 85:
        Text(Point(2.3, 0.7), "IT'S WICKED HOT!").draw(win)
    # elif statement for cold temperature warning
#    elif fahrenheit < 45:
        

    # Display the output and change button
    output.setText(fahrenheit)
    button.setText("Quit")


    # Display the output and exit
    win.getMouse()
    win.close()

    

main()
