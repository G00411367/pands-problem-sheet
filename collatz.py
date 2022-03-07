# This program ask user to input a positive integer
# then outputs the succesive value of :
# if current value is even divide it by 2
# if odd, multiply by 3 and add
# programs end if the current value is 1

n = int(input("please enter a positive integer :"))

# number must be positive
while n <= 0:
    print("Number is not positive ")
    n = int(input("please enter a positive integer :"))
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





