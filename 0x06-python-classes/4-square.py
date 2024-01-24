#!/usr/bin/python3

'''square'''


class Square:
    '''square class'''

    def __init__(self, size=0):
        '''constructor.

        args:
            size: size
        '''
        self.size = size

    @property
    def size(self):
        '''getter'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''return size'''
        return (self.__size ** 2)
