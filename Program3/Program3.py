
# This program takes a user input (height in inches) and returns one of four
# different outcomes, based on the input. An error check is included for any
# instances where the user enters something besides a number.
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# heightInches               float              get user height in inches


print("********************************************************")
print("*                   Michigan's Coaster Kingdom Theme Park                     *")
print("********************************************************")
print("ROLLER COASTER ELIGIBILITY QUALIFIER")


# defining the coaster function
def coaster_height():
    # use a try/except to catch any non floats in the user input
    try:
        # get user input
        heightInches = float(input("Enter your height in inches: "))
        # evaluate user input based on different heights for roller coaster
        if heightInches <= 0:
            print("Hey there partner, there might be an error.")
        elif heightInches > 0 and heightInches < 42:
            print("We have great rides for you in Sponge Bob World!")
        elif heightInches >= 42 and heightInches < 84:
            print("Come on for a ride on the Super Duper Coaster!")
        elif heightInches >= 84:
            print("You are too tall to ride the Super Duper Coaster. Sorry!")
    except ValueError:
        # decide if user has entered something other than a number. Send error message
        # and ask for input to be reentered
        print("That was not a number; please enter a number to continue.")
        coaster_height()
        return


# call the coaster_height function
coaster_height()


