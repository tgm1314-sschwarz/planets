from abc import ABCMeta, abstractmethod

__author__ = 'Gala & Schwarz'


class SolarSystemFactory:
    """
    Class that is used as an interface.

    **methods**:
        * :func:`animation`: is an abstract method
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def animation(self): pass
