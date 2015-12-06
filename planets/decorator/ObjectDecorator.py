from planets.factory.Object import *

__author__ = 'Gala & Schwarz'


class ObjectDecorator(Object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self): pass
