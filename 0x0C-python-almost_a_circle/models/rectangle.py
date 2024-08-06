#!/usr/bin/python3
""" Module Doc"""

from models.base import Base


class Rectangle(Base):
    """ Class Doc"""

    def __init__(self, width, height, x=0, y=0, id=None):
        hw = {"width": width, "height": height}
        xy = {"x": x, "y": y}
        for key, value in hw.items():
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(key))
            if value <= 0:
                raise ValueError("{} must be > 0".format(key))
        for key, value in xy.items():
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(key))
            if value < 0:
                raise ValueError("{} must be >= 0".format(key))

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    def __err(self, name, value, switch):
        """ Error handel"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and switch == "hw":
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and switch == "xy":
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__err("width", value, "hw")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__err("height", value, "hw")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__err("x", value, "xy")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__err("y", value, "xy")
        self.__y = value

    def area(self):
        """ get rectangle area
            Width x Height"""
        return (self.__width * self.__height)

    def display(self):
        """ Show area with #"""
        if self.__y != 0:
            for d in range(self.__y):
                print()
        if self.__height != 0 and self.__width != 0:
            for a in range(self.__height):
                for b in range(self.__width):
                    if self.__x != 0:
                        for c in range(self.__x):
                            print(" ", end="")
                    print("#", end="")
                print()

    def __str__(self):
        return "[Rectangle] (" + str(self.id) + ") "\
                + str(self.__x) + "/" + str(self.__y) + " - "\
                + str(self.__width) + "/" + str(self.__height)
