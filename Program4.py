import random

# This program takes a user input (an integer) and compares it against a random
# generated number in the program. It checks if the user guesses correctly, the
# guess is too low, or too high, and prompts the user to try again. Once the user
# guesses correctly, a counter displays the number of tries.
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# randomNumber               int              generate random number
# userGuess                       int              gets the users guess number
# userTries                       int              try counter
print("********************************************************")
print("*                           Super Duper Guessing Game                             *")
print("********************************************************")

# initializing and declaring the variables
randomNumber = random.randrange(1, 100)
#print(randomNumber) uncomment this, if you want to see the random number
userTries = 0
# while loop that is always True, while the user is guessing. Will break out of the
# loop once the user guesses correctly
while True:
    userGuess = int(input("Enter your guess: "))
    if userGuess == randomNumber:
        userTries +=1
        print("Correct!")
        print("Total number of Guesses: " + str(userTries))
        break
    else:
        userTries += 1
        if userGuess < randomNumber:
            print("Too Low")
        else:
            print("Too High")