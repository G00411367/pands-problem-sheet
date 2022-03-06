# Calculate sqaure root of a positive floating number using Newton-Raphson method
# Author Ioan Domsa

number = float(input("please enter a positive number :"))

def sqrt(number):
    # initial guess, the number or for large numbers start with lalf 
    guess = (number/2)
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





