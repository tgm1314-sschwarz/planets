from OpenGL.GLU import *

from planets.factory.Object import *

__author__ = 'Gala & Schwarz'


class Planet(Object):
    """
        The class Planet is used to create round Objects that represent Plantes.
        **methods**:
        * :func:`__init__`: creates variables for the attributes of the sphere.
        * :func:`create`: creates the sphere.
    """

    def __init__(self, r):
        """
        :param r: radius
        """
        self.r = r

        self.q = gluNewQuadric()
        self.lats = 30
        self.longs = 30

    def create(self):
        """
        creates a Sphere
        """
        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)
