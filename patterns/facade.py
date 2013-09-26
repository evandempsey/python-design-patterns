#!/usr/bin/env python

# Define an abstract base class for the type
# of thing our facade is going to wrap.


class Shape(object):
    """
    Abstract class for Shape objects.
    Must implement the draw() method.
    """

    def draw(self):
        """
        Draw the shape.
        """
        raise NotImplementedError("draw() method is not implemented.")


# Define concrete classes for each specific
# thing the factory is going to produce.

class Rectangle(Shape):
    """
    Class to represent a rectangle.
    """

    def draw(self):
        """
        Draw the rectangle.
        """
        print "inside Rectangle.draw()"


class Square(Shape):
    """
    Class to represent a square.
    """

    def draw(self):
        """
        Draw the square.
        """
        print "inside Square.draw()"


class Circle(Shape):
    """
    Class to represent a circle.
    """

    def draw(self):
        """
        Draw the circle.
        """
        print "inside Circle.draw()"


# Define a facade class.


class ShapeMaker(object):
    """
    Facade for methods on shape objects.
    """

    def __init__(self):
        self.rectangle = Rectangle()
        self.square = Square()
        self.circle = Circle()

    def drawRectangle(self):
        self.rectangle.draw()

    def drawSquare(self):
        self.square.draw()

    def drawCircle(self):
        self.circle.draw()


def main():
    """
    Test the facade pattern implementation.
    """
    shapeMaker = ShapeMaker()
    shapeMaker.drawRectangle()
    shapeMaker.drawSquare()
    shapeMaker.drawCircle()


if __name__ == "__main__":
    main()
