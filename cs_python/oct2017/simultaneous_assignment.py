"""
A simple program to average two numbers
Illustrates use of multiple input
"""

def main():
    print("This program computes the average of two exam scores.")

    score1, score2 = eval(raw_input("\nEnter two scores separated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the scores is:", average)

main()
    
