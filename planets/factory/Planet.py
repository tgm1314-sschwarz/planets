from OpenGL.GLU import *

from planets.factory.Object import *

__author__ = 'Gala & Schwarz'


class Planet(Object):

    def __init__(self, r):
        self.r = r

        self.q = gluNewQuadric()
        self.lats = 30
        self.longs = 30

    def create(self):
        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)
