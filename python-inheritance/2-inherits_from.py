""" 
 inherit from returns true if an object is an instance
 of a class that inherited (directly/indirectly)
"""

def inherits_from(obj, a_class):
    """ my func definition """
    return isinstance(obj, a_class)