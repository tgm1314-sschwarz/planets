from Decorator.PlanetDecorator import PlanetDecorator
from OpenGL.GLU import *


class HasMoon(PlanetDecorator):

    def __init__(self, q, r, lats, longs):
        self.q = q
        self.r = r
        self.lats = lats
        self.longs = longs
        self.create_sphere()

    def create_sphere(self):
        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)