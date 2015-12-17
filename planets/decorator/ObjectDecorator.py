from planets.factory.Object import *

__author__ = 'Gala & Schwarz'


class ObjectDecorator(Object):
    """
    Class that is used as an interface.

    **methods**:
        * :func:`create`: is an abstract method
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self): pass
