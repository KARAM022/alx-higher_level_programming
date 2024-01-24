#!/usr/bin/python3

"""cmnt"""


class Square:
    """cmnt"""

    def __init__(self, size):
        """cmnt
        """
        self.size = size

    @property
    def size(self):
        """cmnt"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """cmnt"""
        return (self.__size * self.__size)

    def my_print(self):
        """cmnt"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
