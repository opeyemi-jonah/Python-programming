# JonahP1
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: provides user capability to calculate 
# volume of a pyramid.
# Python version: 3.12.0
import math

# Length of the base:  a
# Height of the pyramid:  h
# Volume = a^2 * h / 3
# Slant height, s = sqrt(h^2 + (a/2)^2)
# Area of one pyramid side = s * a / 2
# Area of all 4 sides of the pyramid is 4 * Area of one pyramid

# Get user input for base length
a = input("Enter the base length: ")

# Get user input for height of the pyramid
h = input("Enter the pyramid's height: ")

# Convert input to floats for program to run properly
try:
    a = float(a)
    h = float(h)
except ValueError:
    print("Please enter valid numbers for base length and height.")
    exit()

# Calculate the volume
def Volume(base, height):
    v = (math.pow(base, 2) * height) / 3
    print("The volume of the pyramid is: ", v)
    return round(v, 1)

# Calculate slant height
def SlantHeight(base, height):
    s = math.sqrt(math.pow(height, 2) + math.pow(base * 0.5, 2))
    print("Slant height = ", s)
    return round(s, 1)

# Calculate the area of one pyramid side
def AreaOfOnePyramidSide(base, slantHeight):
    oneAreaSide = slantHeight * (base * 0.5)
    print("Area of one pyramid side is: ", oneAreaSide)
    return round(oneAreaSide, 1)

# Calculate the area of all sides of the pyramid
def AreaOfAllSides(area):
    totalArea = 4 * area
    print("The total area of this pyramid is: ", totalArea)
    return round(totalArea, 1)

# Do all the necessary calculations
def CalculateFormulas(base, height):
    volume = Volume(base, height)
    slantHeight = SlantHeight(base, height)
    oneSideArea = AreaOfOnePyramidSide(base, slantHeight)
    totalArea = AreaOfAllSides(oneSideArea)
    return volume, slantHeight, oneSideArea, totalArea

CalculateFormulas(a, h)





