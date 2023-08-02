"""
is_kind_of_class - function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from, the specified
"""

def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class function
    """
    return isinstance(obj, a_class)
