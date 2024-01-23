#!/usr/bin/python3
'''square'''


class Square:
    '''Square class'''

    def __init__(self, size=0):
        '''constructor.

        args:
            size: size
        '''
        self.__size = size

    @property
    def size(self):
        '''getter'''
        return self.__size

    @property.setter
    def size(self, value):
        '''setter

        args:
            value: value
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''current square area.'''
        return self.__size ** 2
