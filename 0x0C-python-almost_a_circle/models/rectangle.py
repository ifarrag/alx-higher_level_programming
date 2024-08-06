#!/usr/bin/python3
""" Module Doc"""

from models.base import Base


class Rectangle(Base):
    """ Class Doc"""

    def __init__(self, width, height, x=0, y=0, id=None):
        def __errinit(self, name, value, switch):
        """ Error handel"""

            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0 and switch == "hw":
                raise ValueError("{} must be > 0".format(name))
            if value < 0 and switch == "xy":
                raise ValueError("{} must be >= 0".format(name))

        self.__errinit("width", width, "hw")
        self.__width = width
        self.__errinit("height", height, "hw")
        self.__height = height
        self.__errinit("x", x, "xy")
        self.__x = x
        self.__errinit("width", y, "xy")
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
