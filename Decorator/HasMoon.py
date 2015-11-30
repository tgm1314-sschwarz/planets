from decorator.ObjectDecorator import ObjectDecorator
from OpenGL.GLU import *


class HasMoon(ObjectDecorator):

    def __init__(self, q, r, lats, longs):
        self.q = q
        self.r = r
        self.lats = lats
        self.longs = longs
        self.create()

    def create(self):
        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)