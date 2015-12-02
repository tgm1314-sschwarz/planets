from OpenGL.GLU import *

from planets.factory.Object import *


class Planet(Object):

    def __init__(self, q, r, lats, longs):
        self.q = q
        self.r = r
        self.lats = lats
        self.longs = longs

    def create(self):
        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)
