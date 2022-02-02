'''Write a program to calculate the area and perimeter of a rectangle.'''
import math
from math import pi
rad = float(input("Enter the radius of the circle\t"))
area = pi * math.pow(rad,2)
perimeter = 2 * pi * rad
print("The area of the circle is ",round(area,3))
print("The perimeter of the circle is ",round(perimeter,3))