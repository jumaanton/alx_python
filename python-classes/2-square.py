""" 
Class Square that defines a square by:
(based on 1-square.py)
"""

class Square:
    """
    A class that defines a square by size.
    """

    def __init__(self, size=0):
        self.__size = 0  # Default size is 0

        # Check if size is provided and is an integer
        if isinstance(size, int):
            # Check if size is non-negative
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
        
