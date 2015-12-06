from abc import ABCMeta, abstractmethod

__author__ = 'Gala & Schwarz'


class SolarSystemFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def animation(self): pass
