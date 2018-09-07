# day1.py
# Mr Watson
# Generate a random integer between 1-100
from random import *

correctNum = randint(1, 100)

tryNum = 0
running = True
while running:
    # Prompt for user's guess
    print ("Enter an integer from 1 to 100 \nEnter '-1' to quit\n")

    # Input user's guess
    guessNum = int(input())

    tryNum += 1

    diff = abs(correctNum - guessNum)

    # Check how close user's guess is to correct
    if guessNum == -1:
        output = "\nThanks for playing!"
        running = False

    elif guessNum > 100:
        output = "\nWAY TOO BIG!\n"

    elif guessNum == correctNum:
        output = "\nYOU GUESSED IT!\n"
        running = False

    elif 1 <= abs(diff) <= 5:
        output = "\nHOT\n"

    elif 5 <= abs(diff) <= 10:
        output = "\nVERY WARM\n"

    elif 10 <= abs(diff) <= 20:
        output = "\nWARM\n"

    elif 20 <= abs(diff) <= 40:
        output = "\nKINDA WARM\n"

    elif 40 <= abs(diff) <= 100:
        output = "\nCOLD\n"

    print (output)

if guessNum != -1:
    print (".. and it only took " + str(tryNum) + " guesses!")

