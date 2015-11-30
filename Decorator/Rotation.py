from OpenGL.GL import *
from decorator.PlanetDecorator import PlanetDecorator


class Rotation(PlanetDecorator):

    def __init__(self, deg, x, y, z):
        self.deg = deg
        self.x = x
        self.y = y
        self.z = z
        self.create()

    def create(self):
        glRotatef(self.deg, self.x, self.y, self.z)
