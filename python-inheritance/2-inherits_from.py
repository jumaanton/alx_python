""" 
 inherit from returns true if an object is an instance
 of a class that inherited (directly/indirectly)
"""


def inherits_from(obj, a_class):
    """
    Return True if an object is an instance
    of a class that inherited (directly or indirectly).

    Args:
        obj (object): The object to check.
        a_class (class): The specified class to check against.

    Returns:
        bool: True if the object is an instance of a subclass 
        of the specified class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
