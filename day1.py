# day1.py
# Mr Watson
# Generate a random integer between 1-100
from random import *

correctNum = randint(1, 100)

# print (correctNum)

tryNum = 0
running = True
while running:
    # Prompt for user's guess
    print ("Enter an integer from 1 to 100 \nEnter '-1' to quit")

    # Input user's guess
    guessNum = int(input())

    tryNum += 1

    diff = abs(correctNum - guessNum)

    # Check how close user's guess is to correct
    if guessNum == -1:
        output = "Quit"
        running = False

    elif guessNum > 100:
        output = "Too High"

    elif guessNum == correctNum:
        output = "You guessed it!"
        running = False

    elif 1 <= abs(diff) <= 5:
        output = "HOT"

    elif 5 <= abs(diff) <= 10:
        output = "VERY WARM"

    elif 10 <= abs(diff) <= 20:
        output = "WARM"

    elif 20 <= abs(diff) <= 40:
        output = "LUKEWARM"

    elif 40 <= abs(diff) <= 100:
        output = "COLD"

    print (output)

print (tryNum)





