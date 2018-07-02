"""
Temperature conversion between Celsius  and Fahrenheit
Python version 2.7.10
Written by Hariharaselvam Balasubramanian
"""
print "Temperature conversion between Celsius and Fahrenheit"
print "*****************************************************"
print "1. Celsius to Fahrenheit"
print "2. Fahrenheit to Celsius"
print ""
option = raw_input("Enter the option ")
if option == "1":
    Celsius = raw_input("Enter Temperature in Celsius : ")
    Fahrenheit = 9.0/5.0 * float(Celsius) + 32
    print "Temperature:", Celsius, "Celsius = ", Fahrenheit, " F"

elif option == "2":
    Fahrenheit = raw_input("Enter a temperature in Fahrenheit : ")
    Celsius = (float(Fahrenheit) - 32) * 5.0/9.0
    print "Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C"

else:
    print "Selected option is not available"
