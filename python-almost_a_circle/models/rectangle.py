"""
This module defines a Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    """ public method area"""
    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height


    """ public method display"""
    def display(self):
        """
        Prints the rectangle to stdout using the '#' character.
        """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)


    """ public method __str__"""
    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)


    @property
    def width(self):
        """Getter method for width."""
        return self.__width


    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """Getter method for height."""
        return self.__height


    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """Getter method for x."""
        return self.__x


    @x.setter
    def x(self, value):
        """Setter method for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value



    @property
    def y(self):
        """Getter method for y."""
        return self.__y


    @y.setter
    def y(self, value):
        """Setter method for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
