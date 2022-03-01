# This program reads in a string
# And outputs every seccond character of the string in reverse order

a = input('Please enter a sentence : ')

# eg sentence: The quick brown fox jumps over the lazy dog.
# syntax for reversing a string 'a' is a[::-1]

areversed = a[::-2]
# print(a)
print('Every 2nd character of the above string in reverse order is : {}' .format(areversed))