from OpenGL.GL import *

from planets.decorator.ObjectDecorator import *

__author__ = 'Gala & Schwarz'


class Rotation(ObjectDecorator):
    """
    Class that is responsible for the rotation

    **methods**:
        * :func:`__init__`: sets the rotation parameters
        * :func:`create`: adds the parameters to Rotatef
    """
    def __init__(self, deg, x, y, z, p):
        """
        :param deg: degrees parameter
        :param x: x coordinate
        :param y: y coordinate
        :param z: z coordinate
        :param p: Planet object
        """
        self.p = p
        self.deg = deg
        self.x = x
        self.y = y
        self.z = z

    def create(self):
        """
        Rotates a Object Planet
        """
        glRotatef(self.deg, self.x, self.y, self.z)
        self.p.create()
