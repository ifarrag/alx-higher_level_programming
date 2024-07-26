#!/usr/bin/python3
"""Rectangle.
    define a Rectangle"""


class Rectangle:
    """ Define Rectangle """
    number_of_instances = 0
    print_symbol = str(#)

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value is None:
            raise TypeError("height must be an integer")
        if type(value) is not int and type(value) is not float:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if value is None:
            raise TypeError("width must be an integer")
        if type(value) is not int and type(value) is not float:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        if self.height != 0 and self.width != 0:
            sym = ""
            for i in range(self.height):
                for n in range(self.width):
                    sym += Rectangle.print_symbol
                if i != self.height - 1:
                    sym += "\n"
            return sym
        else:
            return str("")

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
