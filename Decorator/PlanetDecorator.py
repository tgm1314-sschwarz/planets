from abc import ABCMeta, abstractmethod
from Planet import Planet


class PlanetDecorator(Planet):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self):
        pass
