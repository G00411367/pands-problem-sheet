# Pands Problem Sheet
## Author: Ioan Domsa
## Programing and Scripting 2022

## Weekly Tasks 02 

Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py

* The user is asked to input a person's height in centimetres and weight in kilograms
* The code outputs their BMI

Code
```
weight = float(input("Enter weight (kg): "))
while weight <= 0:
    print("number is not positive")
    weight = float(input("Please enter a positive number: "))
height = float(input("Enter height (cm): "))
while height <= 0:
    print("number is not positive")
    height = float(input("Please enter a positive number: "))
BMI = round((weight * 10000)/(height**2), 2)
print('weight(Kg) is:' + str(weight))
print('height(cm) is:' + str(height))
print('The BMI is (Kg/m\u00b2) {}.' .format(BMI))
```
User is asked to enter weight in kg.

Decimal numebr is requested and the code checks if the number is positive.

In a simillar way user needs to input the hight in cm
BMI is calculated using formula BMI = weight*10000/height^2

** References **

[BMI Formula] 

(https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used.)

## Weekly Tasks 03 

Write a program that asks a user to input a string and outputs every second letter in reverse order.

Call the file secondstring.py

Code
```
a = input('Please enter a sentence : ')
areversed = a[::-2]
# print(a)
print('Every 2nd character of the above string in reverse order is : {}' .format(areversed))
```
* User is asked to enter a sentance, e.g. : The quick brown fox jumps over the lazy dog.
* The code outputs:  .o zletrv pu o wr cu h.

Python has commands for returning a reversed string by using the syntax a[::-1]

For returning every seccond character of the string we need to specify the step -2 instead of -1

** References **

[How to Reverse a String in Python]

(https://www.w3schools.com/python/python_howto_reverse_string.asp)

## Weekly Tasks 04 

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Call the program collatz.py

* The user is asked to input a positive integer
* The code outputs: the value devided by 2 if input is even. If input is odd the code outputs current value multiplied by 3 and add 1

Code
```
n = int(input("please enter a positive integer :"))
while n <= 0:
    print("Number is not positive ")
    n = int(input("please enter a positive integer :"))
numbers = []

numbers.append(n) 
while n > 1: 
        if (n % 2) == 0:
            evenN = int(n/2)
            numbers.append(evenN)
            n = (evenN)
        else:
            oddN = int(n*3 +1)
            numbers.append(oddN)
            n = int(oddN)
print (numbers)
```
User is prompted to enter a positive integer

The input is checked and if it is not positive integer user is noticed and asked again to enter a positive integer

The succesful input is added to a list

Next, the number is checked if it is even or odd and collatz function is applied accordingly

The new result is added to the list

The code stops when the function returns 1

** References **

[Add to a list]

(https://www.programiz.com/python-programming/methods/list/append)

## Weekly Tasks 05 

Write a program that outputs whether or not today is a weekday.

Call the program weekday.py

* By running the program the code outputs weather or not today is weekday 

Code
```
import datetime 

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
date = datetime.datetime.now()

today = date.strftime("%A")

if today in weekDays:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")
  ```
Python has a module for date & time which we is imported in the code 

We create a variable that lists the weekdays from Monday to Friday inclusive

We create a variable which returns current date by using Python datetime module

We extract the day of the week by using syntax:  date.strftime("%A") 

Next, the code checks weather or not the extracted day of the week is the weekday list variable 

If True, the programe prints "Yes, unfortunately today is a weekday"

** References **

[Python Datetime]

(https://www.w3schools.com/python/python_datetime.asp)

## Weekly Tasks 06 

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root

Create your own sqrt function and not use the built in functions x ** .5 or math.sqrt(x) 

Call the file squareroot.py

* The user is asked to input a positive floating number
* The code returns an aproximation of its square root by using Newton-Raphson method

Code
```
number = float(input("please enter a positive number :"))

while number <= 0:     
    print("number is not positive")
    number = float(input("please enter a positive number :"))

def sqrt(number):
    guess = (number/2)
    precision = 0.05
    
    while True :
        root = guess - ((guess**2 - number)/(2 * guess))
        error = abs((root**2) - number)
        if (error <= precision):
            break
        guess = root
    
    return root 
print("the square root is", round(sqrt(number), 2)) 
```

On line research showed that Newton method of successive approximations of real zeros is a good solution.

Formula: Xn+1 = Xn-((Xn^2-a))/2*Xn)

User is asked to input a positive integer. The input is checked weather is positive or not

We define function called sqrt

In order to start the succesive calculation we need an initial guess. This can be any number between 1 and the user input.

We chose to start with a gusess which is half the user input

We choose a precision for the calculation. This is the error between two succesive iterations

The code keeps running the function until the error is smaller than the precision we set 

** References **

[Newton's method of square root]

(https://en.wikipedia.org/wiki/Newton%27s_method)

(https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.)

(http://www.sosmath.com/calculus/diff/der07/der07.html#answer1)

## Weekly Tasks 07 

Write a program that reads in a text file and outputs the number of e's it contains.

The program should take the filename from an argument on the command line.

Call the file es.py

* The user is asked to input the a file name from the comand line
* The code outputs the numbers of e's it contains

Code
```
import os

filename = input("please enter the file name :").strip()
def doReadletter(filename):
   with open(filename, "r") as f:
     text = f.read()
     count_e = text.count("e")
   return count_e

while not os.path.exists(filename):
   print("file does not exist ")
   filename = input("please enter the file name :").strip()
else:
   answer = doReadletter(filename)
   print("The numbers of 'e's in this file is {}" .format(answer))
```
User is asked to input a file name 

We define a function that reads the content of the file and conts the number of e's

The code checks if the file exist

If the file name is not found the user is asked again


** References **

[Python File read and count]

(https://www.w3schools.com/python/ref_file_read.asp)

(https://www.w3schools.com/python/ref_list_count.asp)

## Weekly Tasks 08 

Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Call the file plottask.py

* The program plots x, x2 and x3 on a set of axes
* The plot is saved on a .png file
* Different colours, legend, grid and titles are shown in the plot

Code
```
import numpy as np
import matplotlib.pyplot as plt
step = 0.25 # set a calculation step for the plot to be smoother 
xpoints = np.arange(0, 5, step)

fx = xpoints
gx = np.power(xpoints, 2)
hx = np.power(xpoints, 3)

plt.plot(xpoints, fx, label = "f(x)", color = "b")
plt.plot(xpoints, gx, label = "g(x)", color = "m")
plt.plot(xpoints, hx, label = "h(x)", color = "r")

plt.title("Plots \n f(x)=x, g(x)=x\u00b2, h(x)=x\u00b3")
plt.xlabel("X"); plt.ylabel("f(x), g(x), h(x)")
plt.legend(loc="upper left")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.margins(0)
plt.savefig('Task08-plot.png')
```
We import numpy library, useful in working with arrays, matrices and linear algebra

We import matplotlib.pyplot module. This module works like MATLAB. It has libraries for creating plots, figures, etc.

Define a step variable to allow us to use more points in calculation so the plots can look smoother if wanted

Generate a list of x points evenly spaced at the deined step

The code calculatea the functions using syntax: numpy.power(a, b)

Plot the the functions; label & colour

Add more elements to the plot: title, xlabel, y label, legend, grid, etc.

Make the plot start from origin 0,0

Save the plot to a png file. The plot will look like this

<img src = "https://user-images.githubusercontent.com/98125831/161385295-186f5f72-33f9-48c4-920c-92ad21c4e3e9.png" width=25% height=25%>

** References **

[Python numpy]

(https://www.w3schools.com/python/numpy/numpy_intro.asp)

(https://numpy.org/doc/stable/reference/generated/numpy.arange.html)

[Plotting in Python]

(https://matplotlib.org/stable/tutorials/introductory/pyplot.html#:~:text=pyplot%20is%20a%20collection%20of,In%20matplotlib.)

(https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/)

[Resize Image in github README.md]

(https://gist.github.com/stevecondylios/dcadb4fc73e63f27a3bbcf17e52058bf)

