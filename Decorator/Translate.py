from OpenGL.GL import *

from decorator.PlanetDecorator import PlanetDecorator


class Translate(PlanetDecorator):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.create_sphere()

    def create_sphere(self):
        glTranslatef(self.x, self.y, self.z)
