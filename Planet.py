from abc import ABCMeta, abstractmethod


class Planet:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_sphere(self): pass
