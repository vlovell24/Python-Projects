
# This program takes a user input of a sentence, and capitalizes the first letter of each
# sentence, while leaving any other capitalized letters in their natural state.
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# userString              string               Stores the user input (sentences)
# fullSentence           string                Stores each word from userString to recreate the full sentence
# eachSentence           string                Separated list of each sentence.

def changeASentence():
    userString = input('Enter sentences to be modified: ') # get user input
    fullSentence = '' # empty string to store the concat sentences into later
    eachSentence = list(userString.split('.')) #split the list on a period
    eachSentence.pop() # remove the last list item spaces and the return key are stored in the list, so we remove that
    for i in range(len(eachSentence)): # loop through the list
        eachSentence[i] = eachSentence[i].strip() # remove all the white space
        fullSentence += eachSentence[i][:1].upper() + eachSentence[i][1:] + '. ' # change the first letter of each sentence to a capital, then concat sentence back together with a period
    print('Your modified sentence is: \n' + fullSentence) # print out the modified sentences to the screen on a new line
    yesNo = input('Enter \'y\' to try again.....') # ask if user wants to change another sentence
    if yesNo == 'y': # if yes, rerun the function
        changeASentence()
    else: # if anything else, end the program
        return
changeASentence()