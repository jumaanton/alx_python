""" 
    Square class with private instance attribute size and public instance method
"""

class Square:
    """
        A class that defines a square by size
    """

    def __init__(self, size=0):
        self.__size = 0  # Default size is 0
        self.size = size  # Use the property setter to set the size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        # Check if size is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Check if size is non-negative
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
        
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
                