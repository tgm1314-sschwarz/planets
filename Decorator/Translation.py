from OpenGL.GL import *
from decorator.PlanetDecorator import PlanetDecorator


class Translation(PlanetDecorator):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.create()

    def create(self):
        glTranslatef(self.x, self.y, self.z)
