
# This program takes a user input and converts it to a float. The program then appends the
# user input into a list called lapSpeeds. Once the user types in -1, the program will print out
# the fastest, slowest and average lap entered, as well as a list of each lap entered by the user.
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# lapSpeeds              list                   creates an empty list to push values to
# userInput              float                  gets the user input and assigns it to a float value
# floatList                float                  rounds the sum of the laps, divided by the length of the laps (calculates average)
# count                     int                     counter that starts at 1 and adds the index value to the counter
# roundedLap            float                  rounds the lap time, to the second decimal place

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('>                   FIRST PLACING                     >')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('Race Lap Information')
print('\n')
lapSpeeds = []
def lapInfo():
    userInput = float(input("Enter lap speed for lap or -1 to calculate totals: "))
    while userInput != -1:
        lapSpeeds.append(userInput)
        lapInfo()
        if lapSpeeds == -1:
            break
        print('\n')
        print('Fastest Lap:', round(max(lapSpeeds), 2))
        print('Slowest Lap:', round(min(lapSpeeds), 2))
        averageLap()
        print('\n')
        lapList()
        quit()


def averageLap():
    floatList = round(sum(lapSpeeds) / len(lapSpeeds), 2)
    print('Average Lap:', floatList)

def lapList():
    count = 1
    print('Lap Speeds:')
    for lap in lapSpeeds:
        roundedLap = round(lap, 2)
        print(str(count) + ": " + str(roundedLap))
        count += 1

lapInfo()