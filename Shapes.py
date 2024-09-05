from Shape import *
import math


class Rectangle(Shape):
    def __init__(self, color, length, width):
        """Initialize a rectangle with a specific color, length, and width."""
        super().__init__(color)
        self.length = length
        self.width = width
        self.area = 0
        self.perimeter = 0

    def count_area(self):
        """Calculate and return the area of the rectangle."""
        self.area = self.length * self.width
        return self.area

    def count_perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        self.perimeter = 2 * (self.length + self.width)
        return self.perimeter

    def __str__(self):
        """Return a string representation of the rectangle."""
        return super().__str__() + f', length - {self.length}, width - {self.width}'


class Square(Shape):
    def __init__(self, color, side):
        """Initialize a square with a specific color and side length."""
        super().__init__(color)
        self.side = side
        self.area = 0
        self.perimeter = 0

    def count_area(self):
        """Calculate and return the area of the square."""
        self.area = self.side * self.side
        return self.area

    def count_perimeter(self):
        """Calculate and return the perimeter of the square."""
        self.perimeter = 4 * self.side
        return self.perimeter

    def __str__(self):
        """Return a string representation of the square."""
        return super().__str__() + f', side - {self.side}'


class Circle(Shape):
    def __init__(self, color, radius):
        """Initialize a circle with a specific color and radius."""
        super().__init__(color)
        self.radius = radius
        self.area = 0
        self.perimeter = 0

    def count_area(self):
        """Calculate and return the area of the circle."""
        self.area = math.pi * self.radius ** 2
        return self.area

    def count_perimeter(self):
        """Calculate and return the perimeter of the circle."""
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter

    def __str__(self):
        """Return a string representation of the circle."""
        return super().__str__() + f', radius - {self.radius}'
