#!/usr/bin/env python

# Define an abstract base class for the type
# of thing our factory is going to produce.


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


# Define a factory class to get objects of
# particular concrete classes based on provided information.


class ShapeFactory(object):
    """
    Produces shapes of the requested type.
    """

    def getShape(self, shapeName):
        """
        Read the shape name and construct the right shape.
        """
        if shapeName == "rectangle":
            return Rectangle()
        elif shapeName == "square":
            return Square()
        elif shapeName == "circle":
            return Circle()
        else:
            return None


def main():
    """
    Test the shape factory.
    """
    factory = ShapeFactory()

    rectangle = factory.getShape("rectangle")
    rectangle.draw()

    square = factory.getShape("square")
    square.draw()

    circle = factory.getShape("circle")
    circle.draw()


if __name__ == "__main__":
    main()