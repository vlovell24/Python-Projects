
# This program takes a user input of c, d or x and converts it to uppercase (this
# makes sure that the letter is consistent. It then uses the input to determine
# if it should exit the program, display the grades of a text file, or calculate the
# average grades of the text file. If the user selects 'd', the program will run the
# DisplayScores function, which opens the text file and displays all of the scores
# on the screen. If the user selects 'c', the program will open the text file, add all
# of the lines (or scores) and then divide by the amount of scores in the file.
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# userInput               string              get the user selection
# counter                   int                  an incrementer to move line to line in the text file
# GradesFile              string              stores the file to be opened
# newLine                  string              stores the file line
# ScoresFile              string              stores the file to be opened
# strRead                  string              stores the file line
# ftTotalScores         float               converts the file line to a float

# def menuChoice():
#     try:
#         print("-------------------------------------------------------------------------")
#         print("                           MISS OTHMAR'S CLASS GRADES                     ")
#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print("D: Display Grades")
#         print("C: Calculate Class Average")
#         print("X: Exit")
#         userInput = input("Enter your menu selection: ").upper()
#         if userInput == "D":
#             DisplayScores()
#             menuChoice()
#         elif userInput == "C":
#             CalcAverage()
#             menuChoice()
#         else:
#             return
#     except Error:
#         print('An error has occurred reading the file, please try again.')
#
# def DisplayScores():
#     counter = 0
#     GradesFile = open('grades.txt')
#     while GradesFile:
#         newLine = GradesFile.readline()
#         counter += 1
#         if  not newLine:
#             break
#         print(str(counter) + ': ' + str(newLine))
#     GradesFile.close()
#
# def CalcAverage():
#     scoresFile = open('grades.txt', 'r')
#     strRead = scoresFile.readline()
#     ftTotalScores = float(strRead)
#     counter = 0
#     while strRead != '':
#         strRead = scoresFile.readline()
#         counter += 1
#         if strRead != '':
#             ftTotalScores = float(ftTotalScores) + float(strRead)
#     print(round(ftTotalScores / counter, 2))
#     scoresFile.close()
#
# menuChoice()













