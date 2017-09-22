"""
Program Plan

Show future value of a ten-year investment.
Two inputs: the amount of money to be invested, and the annualized rate of interest.

"""

from graphics import *

def main():
    print("This program plots the growth of a 10-year investment.")

    principal = eval(raw_input("Enter the initial principal: "))
    apr = eval(raw_input("Enter the annualized interest rate: "))
    
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")

    
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 07.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


    for year in range(1,11):

        principal = principal * (1 + apr)

        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    raw_input("Press <Enter> to quit")
    win.close()

main()

        
