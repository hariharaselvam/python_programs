"""
Sigma Value of given number
Python version 2.7.10
Written by Hariharaselvam Balasubramanian
"""

# Factorial Value is the product of the integer and its previous numbers

def factorial_calc(number):
    factorial = 1
    if number not in [0, 1]:
        for i in range(number, 1, -1):
            factorial = factorial * i
    return factorial


# Sigma is the sum of numbers from 1 to n with number
# divided by factorial value of that number and
# multiplied by minus one for even numbers

def sigma_calc(number):
    sigma = 0
    for i in range(1, number + 1):
        sign = -1 if i % 2 == 0 else 1
        sigma = sigma + (sign * (float(i) / factorial_calc(i)))
        if i == 1:
            calculation_str = "1"
        else:
            calculation_str = "%s %s %d/%d!" % (calculation_str, '-' if i % 2 == 0 else '+', i, i)
    return sigma, calculation_str


print "Sigma Calculation"
print "*****************"
input_value = int(raw_input("Enter the number : "))
output_value, calculation_str = sigma_calc(input_value)
print "Calculation is"
print calculation_str
print "Sigma of %d is %f " % (input_value, output_value)
print "--------------------------"
