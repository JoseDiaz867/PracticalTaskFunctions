"""
Task2. Write a program that calculates the area of a rectangle, triangle and circle
(write three functions to calculate the area. And call them in the main program depending on the user's choice).
"""
import math
def rectangle_area() -> float:
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return (height*width)

def triangle_area() -> float :
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return (base*height/2)

def circle_area() -> float:
    radius = float(input("Enter the radius of the circle: "))
    return (math.pi*radius**2)

def calculate_area():
    print("Select the figure type to calculate area, where:")
    print("Enter (1) for rectangle.")
    print("Enter (2) for triangle.")
    print("Enter (3) for circle.")
    figure = input()
    if (figure == "1"):
        area = rectangle_area()
    elif(figure == "2"):
        area = triangle_area()
    elif(figure == "3"):
        area = circle_area()
    else:
        area = None
    return area

# Test:
print(calculate_area())