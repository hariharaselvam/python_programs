"""
Area Calculation for different shapes
Python version 2.7.10
Written by Hariharaselvam Balasubramanian
"""


def area_of_square(base):
    # Area of Square
    # area = base power 2
    return base ** 2


def area_of_rectangle(length, breadth):
    # Area of Rectangle
    # area = length * breadth
    return length * breadth


def area_of_triangle(a, b, c):
    # Area of Triangle
    # surface = ( side 1 + side 2 + side ) / 2
    # area = ( surface * ( surface - side 1 ) * ( surface - side 2 ) * ( surface - side 3 ) power 2
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def area_of_circle(radius):
    # Area of Circle
    # area = pi * radius square
    pi = 3.14159
    return pi * radius ** 2


option = ""
output_value = 0
print "Area Calculation program"
print "************************"
while option != "0":
    print "------------------------------------------"
    print "Area of shapes"
    print "1. Square"
    print "2. Rectangle"
    print "3. Triangle"
    print "4. Circle"
    print "0. Exit"
    print ""
    option = raw_input("Enter the option : ")
    if option == "1":
        print "\nSquare Selected\n"
        input_value = raw_input("Enter the side   : ")
        side = float(input_value)
        output_value = area_of_square(side)
        print "The area of square is " + str(output_value)

    elif option == "2":
        print "\nRectangle Selected\n"
        input_value_1 = raw_input("Enter the width  : ")
        width = float(input_value_1)
        input_value_2 = raw_input("Enter the length : ")
        length = float(input_value_2)
        output_value = area_of_rectangle(width, length)
        print "The area of rectangle is " + str(output_value)

    elif option == "3":
        print "\nTriangle Selected\n"
        input_value_1 = raw_input("Enter the side 1 : ")
        side_1 = float(input_value_1)
        input_value_2 = raw_input("Enter the side 2 : ")
        side_2 = float(input_value_2)
        input_value_3 = raw_input("Enter the side 3 : ")
        side_3 = float(input_value_3)
        output_value = area_of_triangle(side_1, side_2, side_3)
        print "The area of triangle is " + str(output_value)

    elif option == "4":
        print "\nCircle Selected\n"
        input_value = raw_input("Enter the radius : ")
        radius = float(input_value)
        output_value = area_of_circle(radius)
        print "The area of circle is " + str(output_value)

    elif option == "0":
        print "\nExit Selected\n"
        break

    else:
        print "Selected option is not available"
