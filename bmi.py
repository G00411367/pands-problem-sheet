# Calculate bmi
# Author: Ioan Domsa

# Inputs
weight = 65
height = 180

# BMI formula; round 2 decimals
BMI = round((weight * 10000)/(height**2), 2)

print('weight(Kg) is:' + str(weight))
print('height(cm) is:' + str(height))
print('The BMI(Kg/m2) is: {}' .format(BMI))




