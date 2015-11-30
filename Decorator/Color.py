from OpenGL.GL import *
from decorator.PlanetDecorator import PlanetDecorator


class Color(PlanetDecorator):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.create()

    def create(self):
        glColor3f(self.r, self.g, self.b)
