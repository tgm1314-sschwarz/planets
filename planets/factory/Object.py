from abc import ABCMeta, abstractmethod

__author__ = 'Gala & Schwarz'


class Object:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self): pass
