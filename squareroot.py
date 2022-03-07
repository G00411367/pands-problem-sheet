# Calculate sqaure root of a positive floating number using Newton-Raphson method
# Author Ioan Domsa

number = float(input("please enter a positive number :"))

# number needs to be positive
while number <= 0:     
    print("number is not positive")
    number = float(input("please enter a positive number :"))

# define the function
def sqrt(number):
    # initial guess can start with half of the number 
    guess = (number/2)
    # accuracy of root calculation
    precision = 0.05
    
    while True :
        # Newtons calculus
        root = guess - ((guess**2 - number)/(2 * guess))
        # check error difference 
        error = abs((root**2) - number)
        if (error <= precision):
            break
        # update root
        guess = root
    
    return root 
print("the square root is", round(sqrt(number), 2))





