

# This program takes a user input of c, d or x and converts it to uppercase (this
# makes sure that the letter is consistent. It then uses the input to determine
# if it should exit the program, show a display of menu options, or run a calculation
# that determines cost of admission to the escape room. The cost of admission is
# based on two variables. The number of visitors and the amount of time in the room.
# A 5% tax is added onto the total cost, and then returned to the main function, so
# that a individual cost per person can be calculated.
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# userInput               string              get the user selection
# visitors                   int                  gets the number of visitors
# minutes                    int                 gets the number of minutes
# groupCost                float              cost for the group
# perPersonCost          float              cost per person
# serviceFee               float              additional tax
print("===============================================================")
print("                             Escape Artists Escape Room                               ")
print("===============================================================")

# defining the menuChoice function. This gives the user the menu options in the
# program
def menuChoice():
    print("Menu of options")
    print("C: Calculate admission cost")
    print("D: Display admission options")
    print("X: Exit application")
    userInput = input("Enter your menu selection: ").upper()
    if userInput == "D":
       displayFees()
    elif userInput == "C":
       calculateAdmission()
    elif userInput == "X":
        return
    else:
        print("Invalid selection, please try again.")
        menuChoice()

#defining the displayFees function. This displays the fees based on minutes in the
# escape room
def displayFees():
    print("********************************")
    print("MENU OF CHOICES")
    print("********************************")
    print("35 Minutes                              $85.00")
    print("60 Minutes                             $130.00")
    print("75 Minutes                             $155.00")
    input("press enter to return to menu:")
    menuChoice()
# defining the calculateAdmission function. This function calculates the admission fees for the group
# and per person, and displays it on the screen
def calculateAdmission():
    visitors = int(input("Number of visitors: "))
    minutes = int(input("Number of minutes (35, 60, 75) : "))
    if minutes == 35:
        subtotal = 85.00
        groupCost = "${:,.2f}".format(calcServiceFee(subtotal) + subtotal)
        perPersonCost = "${:,.2f}".format((calcServiceFee(subtotal) + subtotal) / visitors)
        print("GROUP COST: " + groupCost)
        print("PER PERSON COST: " + perPersonCost)
        input("press enter to return to menu:")
        menuChoice()
    elif minutes == 60:
        subtotal =  130.00
        groupCost = "${:,.2f}".format(calcServiceFee(subtotal) + subtotal)
        perPersonCost = "${:,.2f}".format((calcServiceFee(subtotal) + subtotal) / visitors)
        print("GROUP COST: " + groupCost)
        print("PER PERSON COST: " + perPersonCost)
        input("press enter to return to menu:")
        menuChoice()
    else:
        subtotal = 155.00
        groupCost = "${:,.2f}".format(calcServiceFee(subtotal) + subtotal)
        perPersonCost = "${:,.2f}".format((calcServiceFee(subtotal) + subtotal) / visitors)
        print("GROUP COST: " + groupCost)
        print("PER PERSON COST: " + perPersonCost)
        print("press enter to return to menu:")
        menuChoice()
# defining the calcServiceFee function. This calculates the additional 5% tax
def calcServiceFee(subtotal):
    serviceFee = subtotal * .05
    return serviceFee


menuChoice()