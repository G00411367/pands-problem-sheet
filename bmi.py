# Calculate bmi
# Author: Ioan Domsa

# Input weight
weight = float(input("please enter weight :"))
# input has to be a positive number
while weight <= 0:
    print("number is not positive")
    weight = float(input("please enter a positive number :"))

# Input height
height = float(input("please enter height :"))
# input has to be a positive number
while height <= 0:
    print("number is not positive")
    height = float(input("please enter a positive number :"))

# BMI formula; round 2 decimals
BMI = round((weight * 10000)/(height**2), 2)

print('weight(Kg) is:' + str(weight))
print('height(cm) is:' + str(height))
print('The BMI(Kg/m2) is: {}' .format(BMI))




