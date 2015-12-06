from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from planets.decorator.ObjectDecorator import *

__author__ = 'Gala & Schwarz'


class Moon(ObjectDecorator):

    def __init__(self, r, p):
        self.p = p
        self.r = r

        self.q = gluNewQuadric()
        self.lats = 30
        self.longs = 30

    def create(self):
        glPushMatrix()

        glColor3f(.1, .1, .1)
        glutWireTorus(0.05, self.r, self.lats, self.longs)

        glTranslatef(2.0, .0, .0)

        glColor3f(.5, .5, .5)

        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)

        glPopMatrix()
        self.p.create()
