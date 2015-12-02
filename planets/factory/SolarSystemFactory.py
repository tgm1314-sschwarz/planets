from abc import ABCMeta, abstractmethod


class SolarSystemFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def animation(self): pass
