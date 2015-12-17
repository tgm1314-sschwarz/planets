from abc import ABCMeta, abstractmethod

__author__ = 'Gala & Schwarz'


class Object:
    """
        Creats an object.
        **methods**:
        * :func:`create`: creats an object.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self): pass
