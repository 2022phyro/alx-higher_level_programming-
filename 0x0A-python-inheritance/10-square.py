#!/usr/bin/python3
"""This module contains a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a subclass of the Rectangle class
    and a grandchild of the BaseGeometry class

    Args:
        Rectangle (class): The parent class
    """
    def __init__(self, size):
        """Initializes the class

        Args:
            size (int): the dimensions for the square
        """
        self.integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size
