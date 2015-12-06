from OpenGL.GL import *
from OpenGL.GLUT import *

from planets.decorator.ObjectDecorator import *

__author__ = 'Gala & Schwarz'


class Orbit(ObjectDecorator):

    def __init__(self, r, p):
        self.p = p
        self.r = r

        self.lats = 100
        self.longs = 100

    def create(self):
        glPushMatrix()

        glRotatef(-90, 1., .0, .0)
        glColor3f(.1, .1, .1)
        glutWireTorus(0.05, self.r, self.lats, self.longs)

        glPopMatrix()

        self.p.create()
