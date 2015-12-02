from planets.factory.Object import *


class ObjectDecorator(Object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self): pass
