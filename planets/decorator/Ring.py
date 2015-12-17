from OpenGL.GL import *
from OpenGL.GLUT import *

from planets.decorator.ObjectDecorator import *

__author__ = 'Gala & Schwarz'


class Ring(ObjectDecorator):
    """
    Class that creates a torus for a planet (saturn ring)

    **methods**:
        * :func:`__init__`: sets the radius parameter and the Planet Object
        * :func:`create`: Creates and draws a WireTorus Object
    """
    def __init__(self, r, p):
        """
        :param r: radius parameter
        :param p: Planet Object
        """
        self.p = p
        self.r = r

    def create(self):
        """
        Creats the glutWireTour in a Push and Pop Matrix
        """
        glPushMatrix()

        glColor3f(.8, .8, .8)
        glRotatef(-90, 1., .0, .0)

        for i in range(self.r):
            glutWireTorus(0.1, 2+(i*0.1), 30, 30)

        glPopMatrix()

        self.p.create()
