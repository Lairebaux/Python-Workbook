"""Python Workbook
Exercise 18: Volume of a Cylinder
Modified to include volume and area of many shapes
"""

import math
from abc import ABC, abstractmethod


class Shapes(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass

class Circle(Shapes):

    def __init__(self, diameter=None):
        self.diameter = diameter
        self.radius = diameter / 2
        self.pi = math.pi

    def area(self):
        """area of a circle"""
        return f"{self.pi * (self.radius ** 2):.2f}"

    def perimeter(self):
        """circumference of a circle"""
        return f"{self.pi * self.diameter:.2f}"


class Sphere(Circle, Volume):

    def area(self):
        """area of a sphere"""
        return f"{(self.pi * 4 ) * (self.radius ** 2):.2f}"

    def volume(self):
        """volume of a circle"""
        return f"{(self.pi * 4/3) * (self.radius ** 3):.2f}"


class Rectangle(Shapes, Volume):
    def __init__(self, length=None, width=None, height=None):
        self.l = length
        self.w = width
        self.h = height

    def area(self):
        """area of rectangle"""
        return f"{self.l * self.w:.2f}"

    def perimeter(self):
        """circumference of a circle"""
        return f"{2* (self.l + self.w):.2f}"

    def volume(self):
        """volume of a rectangle"""
        return f"{self.l * self.w * self.h:.2f}"


class Cone(Circle, Volume):

    def __init__(self, diameter=None, height=None, slant=None):
        Circle.__init__(self, diameter)
        self.h = height
        self.s = slant

    def area(self):
        """area of a pyramid with square base"""
        return f"{(self.pi * self.radius ** 2) + (self.pi * self.radius) * self.s:.2f}"

    def volume(self):
        """volume of a cone"""
        return f"{(1/3 * self.pi) *(self.radius ** 2) * self.h:.2f}"
