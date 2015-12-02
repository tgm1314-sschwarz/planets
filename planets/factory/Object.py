from abc import ABCMeta, abstractmethod


class Object:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self): pass
