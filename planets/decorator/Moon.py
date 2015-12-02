from OpenGL.GLU import *

from planets.decorator.ObjectDecorator import *


class Moon(ObjectDecorator):

    def __init__(self, q, r, lats, longs, p):
        self.p = p
        self.q = q
        self.r = r
        self.lats = lats
        self.longs = longs
        self.create()

    def create(self):
        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)
        self.p.create()
