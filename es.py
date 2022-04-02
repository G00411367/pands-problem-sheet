# This program reads in a text file from a command line argument
# and outputs the number of e's it contains 

# Author: Ioan Domsa

import os
# ask user to specify the file name

filename = input("please enter the file name :").strip()
# define a function that reads the number of characters "e"
def doReadletter(filename):
   with open(filename, "r") as f:
     text = f.read()
     count_e = text.count("e")
   return count_e

# check the file name exists or if it is correct
while not os.path.exists(filename):
   print("file does not exist ")
   filename = input("please enter the file name :").strip()
else:
   answer = doReadletter(filename)
   print("The numbers of 'e's in this file is {}" .format(answer))




