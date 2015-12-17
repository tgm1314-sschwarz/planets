from OpenGL.GL import *
from OpenGL.GLUT import *

from planets.decorator.ObjectDecorator import *

__author__ = 'Gala & Schwarz'


class Orbit(ObjectDecorator):
    """
    Class that creates a torus orbit for the planets

    **methods**:
        * :func:`__init__`: sets the radius parameter and the Planet Object and lats and longs
        * :func:`create`: Creates and draws a WireTorus Object
    """
    def __init__(self, r, p):
        """
        sets the button name
        :param r: radius
        :param p: planet object
        """
        self.p = p
        self.r = r

        self.lats = 100
        self.longs = 100

    def create(self):
        """
        creates a glutWireTorus Object
        """
        glPushMatrix()

        glRotatef(-90, 1., .0, .0)
        glColor3f(.1, .1, .1)
        glutWireTorus(0.05, self.r, self.lats, self.longs)

        glPopMatrix()

        self.p.create()
