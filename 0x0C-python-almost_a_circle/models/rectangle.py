#!/usr/bin/python3
""" Module Doc"""

from models.base import Base


class Rectangle(Base):
    """ Class Doc"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    def __err(name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and value is not x and value is not y:
            raise ValueError(f"{name} must be > 0")
        if value is y or value is x and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__err("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__err("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__err("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__err("y", value)
        self.__y = value

    def area(self):
        """ get rectangle area
            Width x Height"""

        return (self.__width * self.__height)
