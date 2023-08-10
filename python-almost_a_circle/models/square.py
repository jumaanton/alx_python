""" class square that inherits from rectangle """

from models.rectangle import Rectangle

""" class square that inherits from rectangle """
class Square(Rectangle):
    """ class consotructor """
    def __init__(self, size, x=0, y=0, id=None):
        """  super class with id, x, y, width and height - 
        this super call will use the logic of the __init__ 
        of the Rectangle class. """
        super().__init__(size, size, x, y, id)

    """ overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height"""
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


    """ getter and setter for size """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value
        
        
