'''
Author: mianmiantea2019
Date: 2023-05-01 12:06:38
LastEditors: mianmiantea2019
LastEditTime: 2023-05-01 14:13:42
Description: 
'''
# Use the input() function to get keyboard input (string)
# Use the int() function to convert the input string to an integer
# Use the print() function to output a string with placeholders

# The string output in the print function above uses placeholder syntax, where %d is a placeholder for integers, %f is a placeholder for decimals, %% represents a percent sign (because the percent sign represents a placeholder, so the string with placeholders must be written as %%) to represent the percent sign, and the variable value followed by % after the string will replace the placeholder and then output to the terminal, run the above program and see the program execution result.

# a = int(input('a = '))
# b = int(input('b = '))

# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))


# a = 10
# b = 3
# a += b        
# a *= a + 2  #15*13  
# print(a)      

a = 10
b = 3
result = a % b
print("{} % {} = {}".format(a, b, result)) # 1



# Addition
a = 10
b = 3.5
result = a + b
print("The sum of {} and {} is {}".format(a, b, result))

# Subtraction
a = 15
b = 7.2
result = a - b
print("The difference between {} and {} is {}".format(a, b, result))

# Multiplication
a = 4
b = 2.5
result = a * b
print("{} times {} is {}".format(a, b, result))

# Division
a = 10
b = 3
result = a / b
print("{} divided by {} is {}".format(a, b, result))

# Integer Division
a = 10
b = 3
result = a // b
print("{} divided by {} is {} with a remainder of {}".format(a, b, result, a % b))

# Exponentiation
b = 3
result = a ** b
print("{} raised to the power of {} is {}".format(a, b, result)) 

