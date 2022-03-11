# This program reads in a text file from acommand line argument
# and outputs the number of e's it contains

import os
# ask user to specify the file name

filename = input("please enter the file name :")
letter = "e"
def doReadE(filename, letter):
   with open(filename, "rt") as f:
    text = f.read()
    return text.count(letter)

if os.path.exists(filename):
   answer = doReadE(filename, letter)
   print(answer)
else:
  print("file does not exist ")
  print("please try again ")
