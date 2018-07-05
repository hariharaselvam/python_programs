"""
Fibonacci Series
Python version 2.7.10
Written by Hariharaselvam Balasubramanian
"""
print "Fibonacci Series Program"
print "************************"

# Fibonacci Series is the integer sequence where each element is the sum of previous two numbers
# Example Series is 0, 1, 1, 2, 3 ......

length_of_series = int(raw_input("Enter the length of series : "))

first_value = 0
second_value = 0
fibonacci_series = []

for i in range(length_of_series):
    element = first_value + second_value
    fibonacci_series.append(element)
    if i == 0:
        first_value = 0
        second_value = 1
    else:
        first_value = fibonacci_series[i - 1]
        second_value = fibonacci_series[i]
print "First %d fibonacci series are : " % (length_of_series)
print fibonacci_series
print "------------------------"
