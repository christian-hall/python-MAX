# Chapter 7 - Classes & Methods
# could also 'import circle'
# could also 'import circle as cir'
from circle import Circle

# going to create a class within a python script (creating classes that are their own files later)
# in python, the 'pass' keyword can be used in the absence of any other real code to prevent errors
# """docstring""" - hover over a class and this string will show up. Docstrings are optional
# Variables and methods inside classes are attributed to classes themselves
class Rectangle:
    """Rectangle class holds length and width attributes"""
    area_formula = "area = length * width"

    # This is a constructor. You have to create an init method to construct an object
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """calculate the are of the rectangle"""
        return self.length * self.width

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        return self.length * 2 + self.width * 2


rectangle_1 = Rectangle(5, 6)
rectangle_2 = Rectangle(10, 25)
circle_1 = Circle(3)
circle_2 = Circle(5)

print(f'Rectangle 1 Area = {rectangle_1.area()}')
print(f'Rectangle 1 Perimeter = {rectangle_1.perimeter()}')
print(f'Rectangle 2 Area = {rectangle_2.area()}')
print(f'Rectangle 2 Perimeter = {rectangle_2.perimeter()}')
print(f'Circle 1 area = {circle_1.area()}')
print(f'Circle 2 area = {circle_2.area()}')
# print a property in an object
print(f'Circle 1 radius = {circle_1.radius}')