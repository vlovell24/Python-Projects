
# This program takes a user input of a sentence, and capitalizes the first letter of each
# sentence, while leaving any other capitalized letters in their natural state.
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# dailyArray              list               Stores the daily rate
# milesArray              list               Stores the mileage rate
# weeklyArray           list               Stores the weekly rate
# userInput               string            Stores the user input value for the first selection
# choice                    string             Stores the user input for daily or weekly selection
# dailyDays               float              Stores the user input for amount of days the truck is needed
# dailyMiles              float              Stores the user input for amount of miles will be used on the truck
# dailyCost                float             Calculates the final cost to rent the truck
# weeks                     float             Stores the user input for amount of weeks the truck is needed
# weekMiles             float               Stores the user input for amount of miles they will be driving
# weeklyCost            float               Calculates the weekly cost if under 200 miles
# weeklyCostB          float                Calculates the weekly cost if over 200 miles


def main():
    dailyArray = [17.95, 27.95, 37.95] # list to store daily rate values
    milesArray = [.49, .69, .79] # list to store price per mile
    weeklyArray = [107.79, 166.59, 237.99] # list to store weekly rates
    print("-------------------------------------------------------------------------")
    print("                                TRUCK RENTAL RATES                                 ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    userInput = input("Select your truck classification (A, B, or C):  or select X to exit: ").upper() # gets truck classification from user, converts to uppercase
    while userInput != "X": # while loop that will terminate the program on x being selected
        if userInput == "A":
            menu(userInput, dailyArray[0], milesArray[0], weeklyArray[0]) # places index 0 from three lists above into condition. Calls menu function
            break
        elif userInput == "B":
            menu(userInput, dailyArray[1], milesArray[1], weeklyArray[1]) # places index 1 from three lists above into condition. Calls menu function
            break
        elif userInput == "C":
            menu(userInput, dailyArray[2], milesArray[2], weeklyArray[2]) # places index 2 from three lists above into condition. Calls menu function
            break
        else:
            print("Not a valid selection, please try again") # if user selects anything other than a, b, c or x; will print this error message
            main() # reruns the program
            break

def menu(line, daily, miles, weekly): #function with the daily, miles, and weekly array values passed into it; as well as the value of the user input from above
        print("-------------------------------------------------------------------------")
        print(f"                      {line} CLASS DAILY/WEEKLY RATES                    ") # places the user input into the print statement
        print("-------------------------------------------------------------------------")
        print(f"Base Daily Charge: ${daily}") # places the dailyArray index value into the print statement
        print(f"Mileage Charge (Daily Rental): {miles} per mile") # places the milesArray index value into the print statement
        print(f"Base Weekly Charge: ${weekly}") # places the weeklyArray index value into the print statment
        print(f"Mileage Charge (Weekly Rental): ${miles} per mile after first 200 miles per week.") # places the milesArray index value into the print statement
        choice = input("Enter D for daily rate calculation or W for weekly rate calculation: ").upper() # gets user input choice of d or w
        if choice == "D":
            try: # try except type error. Will run if user selects a float value in the input statments below
                dailyDays = float(input("How many days?: ")) # asks user for how many days they need to rent the truck; converts to float
                dailyMiles = float(input("How many miles?: ")) # asks the user how many miles they will use; converts to float
                dailyCost = "${:,.2f}".format(float(round(daily * dailyDays + dailyMiles * miles, 2))) # creates a variable that is the calculation of the daily rate * the number of days + the mile rate * the number of miles
                print(f"You want the truck for {int(dailyDays)} days and will be driving {int(dailyMiles)} miles. It will cost {dailyCost}.") # prints out the days and miles needed the truck for; and gives a final price to the user.
                main() #reruns the program
            except ValueError: # will error if user selects a string value and rerun the program
                print("That was not a number, please try again: ")
                main() #reruns the program
        elif choice == "W": #if user choice is w for weekly
            try: #try except error. Checks for correct type of float
                weeks = float(input("How many weeks?: ")) #asks user for the amount of weeks they need the truck for
                weekMiles = float(input("How many miles?: ")) #asks the user for the amount of miles they will be driving
                if weekMiles < 200: #if statement for if the miles are less than 200
                    weeklyCost = "${:,.2f}".format(float(round(weekly * weeks, 2))) #sets a variable to a calculation of the weekly rate * the weeks rented for
                    print( f"You want the truck for {int(weeks)} weeks, and will be driving {weekMiles} miles. It will cost {weeklyCost}.") #prints out the result to the user
                    main() #reruns the program
                else: #else statement that is used if the miles are over 200
                    mileageBMinus = weekMiles - 200 #subtract 200 miles from the total miles
                    weeklyCostB = "${:,.2f}".format(float(round(weekly * weeks + mileageBMinus * miles, 2))) #weekly rate * number of weeks + mileageBMinus variable * number of miles formats it to currency
                    print( f"You want the truck for {int(weeks)} weeks, and will be driving {int(weekMiles)} miles. It will cost {weeklyCostB}.") #prints out the result to the user
                    main() #reruns the program
            except ValueError: #except error that runs if the user enters anything other than a number
                print("That was not a number, please try again:") #print error to screen
                main() #rerun the program
        else: #runs if the user selects anything other than w or d
            print("You have entered an invalid selection, please try again: ") #prints error out to screen
            main() #reruns the program

main()






