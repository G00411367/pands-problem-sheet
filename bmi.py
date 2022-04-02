# Calculate BMI of a person
# Author: Ioan Domsa


# request to input weight; input can be a decimal
weight = float(input("Enter weight (kg): "))
# input has to be a positive number
while weight <= 0:
    print("number is not positive")
    weight = float(input("Please enter a positive number: "))

# request to input height; input can be decimal
height = float(input("Enter height (cm): "))
# input has to be a positive number
while height <= 0:
    print("number is not positive")
    height = float(input("Please enter a positive number: "))

# calculate BMI using formula: BMI=weight/height^2; round 2 decimals
BMI = round((weight * 10000)/(height**2), 2)

print('weight(Kg) is:' + str(weight))
print('height(cm) is:' + str(height))
print('The BMI is (Kg/m\u00b2) {}.' .format(BMI))




