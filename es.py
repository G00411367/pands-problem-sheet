# This program reads in a text file from a command line argument
# and outputs the number of e's it contains

import os
# ask user to specify the file name
filename = input("please enter the file name :").strip()
letter_e = "e"
letter_E = "E"

# define a function that reads the number of characters
def doReadletter(filename, letter_e, letter_E):
   with open(filename, "rt") as f:
    text = f.read()
    count_e = text.count(letter_e)
    count_E = text.count(letter_E)
    countletter = count_e + count_E
    return countletter
# check the file name exists or is correct
while not os.path.exists(filename):
   print("file does not exist ")
   filename = input("please enter the file name :").strip()
else:
   answer = doReadletter(filename, letter_e, letter_E)
   print("The numbers of capital & lowercase 'e's in this file is {}" .format(answer))





