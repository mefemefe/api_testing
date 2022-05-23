"""
Useful metaclasses used to define the behavior of python classes.

Classes:
    Singleton
"""

class Singleton(type):
    """Pythonic Meta Class used to create Singleton classes and it also covers inheritance."""
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
