# This program ask user to input a positive integer
# then it outputs the succesive values of calculation:
# at each step calculate the next value by taking current value and 
# if it is even divide it by 2, but 
# if odd, multiply by 3 and add 1
# programs end if the current value is 1

# Author: Ioan Domsa

n = int(input("Please enter a positive integer: "))

# number must be positive
while n <= 0:
    print("This is not a positive integer ")
    n = int(input("Please enter a positive integer :"))
numbers = []

# add first number to the list
numbers.append(n) 
while n > 1: 
        if (n % 2) == 0:
            evenN = int(n/2)
            numbers.append(evenN) # add even number to the list
            n = (evenN)
        else:
            oddN = int(n*3 +1)
            numbers.append(oddN) # add odd numeber to the list
            n = int(oddN)
print (numbers)





