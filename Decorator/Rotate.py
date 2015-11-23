from OpenGL.GL import *

from Decorator.PlanetDecorator import PlanetDecorator


class Rotate(PlanetDecorator):

    def __init__(self, deg, x, y, z):
        self.deg = deg
        self.x = x
        self.y = y
        self.z = z
        self.create_sphere()

    def create_sphere(self):
        glRotatef(self.deg, self.x, self.y, self.z)
