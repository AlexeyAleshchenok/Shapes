class Shape:
    def __init__(self, color):
        """Initialize a shape with a specific color."""
        self.color = color
        self.area = 0
        self.perimeter = 0

    def set_color(self, color):
        """Set the color of the shape."""
        self.color = color

    def get_color(self):
        """Return the color of the shape."""
        return self.color

    def __str__(self):
        """Return a string representation of the shape."""
        return f'Color - {self.color}'
