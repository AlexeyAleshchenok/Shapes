"""
author: Alexey Aleshchenok
date: 2024-09-02
"""
from Shapes import *
import math
import random

COLORS = ["Red", "Green", "Blue", "Yellow", "Black", "White"]


class Container:
    def __init__(self):
        """Initialize an empty container for storing shapes."""
        self.shapes = []

    def generate(self, x):
        """Generate x random shapes and add them to the container."""
        for _ in range(x):
            shape_type = random.choice(['Rectangle', 'Square', 'Circle'])
            color = random.choice(COLORS)
            if shape_type == 'Rectangle':
                length = random.randint(1, 10)
                width = random.randint(1, 10)
                self.shapes.append(Rectangle(color, length, width))
            elif shape_type == 'Square':
                side = random.randint(1, 10)
                self.shapes.append(Square(color, side))
            else:
                radius = random.randint(1, 10)
                self.shapes.append(Circle(color, radius))

    def sum_areas(self):
        """Calculate and return the total area of all shapes in the container."""
        res = 0
        for shape in self.shapes:
            shape.count_area()
            res += shape.area
        return res

    def sum_perimeters(self):
        """Calculate and return the total perimeter of all shapes in the container."""
        res = 0
        for shape in self.shapes:
            shape.count_perimeter()
            res += shape.perimeter
        return res

    def count_colors(self):
        """Return a string representation of all shapes in the container."""
        color_count = {'Red': 0, 'Green': 0, 'Blue': 0, 'Yellow': 0, 'Black': 0, 'White': 0}
        for shape in self.shapes:
            color_count[shape.get_color()] += 1
        return color_count

    def __str__(self):
        res = ''
        for shape in self.shapes:
            res += shape.__str__() + '\n'
        return res


def add_shapes(shape1, shape2):
    """Add two shapes together, returning a new shape with combined dimensions."""
    if isinstance(shape1, Rectangle) and isinstance(shape2, Rectangle):
        return Rectangle(shape1.color, shape1.length + shape2.length, shape1.width + shape2.width)
    elif isinstance(shape1, Square) and isinstance(shape2, Square):
        return Square(shape1.color, shape1.side + shape2.side)
    else:
        raise TypeError('Addition not supported between these shapes!')


def main():
    """Main function"""
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    rectangle = Rectangle('Black', 5, 10)
    assert rectangle.count_area() == 50
    assert rectangle.count_perimeter() == 30

    square = Square('Black', 5)
    assert square.count_area() == 25
    assert square.count_perimeter() == 20

    circle = Circle('Black', 5)
    assert circle.count_area() == math.pi * 25
    assert circle.count_perimeter() == math.pi * 10
    main()
