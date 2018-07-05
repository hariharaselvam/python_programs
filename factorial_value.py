"""
Factorial Value of given number
Python version 2.7.10
Written by Hariharaselvam Balasubramanian
"""

# Factorial is the product integer and all integers below than it
# The Factorial Value of 6 wil be as 6 * 5 * 4 * 3 * 2 * 1 = 720 = 6!

def factorial_calc(number):
    factorial = 1
    if number not in [0, 1]:
        for i in range(number, 1, -1):
            factorial = factorial * i
    return factorial


print "Factorial Number"
print "****************"
input_value = int(raw_input("Enter the number : "))
output_value = factorial_calc(input_value)
print "Factorial of %d is %d " % (input_value, output_value)
print "--------------------------"
