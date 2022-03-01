# This program ask user to input a positive integer
# then outputs the succesive value of :
# if current value is even divide it by 2
# if odd, multiply by 3 and add
# programs end if the current value is 1

n = int(input("please enter a positive integer :"))
# numbers = []

if n < 0:
    print("Number is not positive ")
    n = int(input("please enter a positive integer :"))
numbers = []

numbers.append(n) # add first number to the list

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

# else:
    # print ("number entered is not a positive integer :")
    # n = int(input ("please eneter again :"))




