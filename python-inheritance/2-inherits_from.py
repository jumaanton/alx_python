""" 
 inherit from returns true if an object is an instance
 of a class that inherited (directly/indirectly)
"""


def inherits_from(obj, a_class):
    """ 
        my func definition 
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
    