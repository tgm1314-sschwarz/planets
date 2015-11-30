from abc import ABCMeta, abstractmethod
from Object import Object


class ObjectDecorator(Object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self): pass
