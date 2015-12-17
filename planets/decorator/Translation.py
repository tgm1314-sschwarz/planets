from OpenGL.GL import *

from planets.decorator.ObjectDecorator import *

__author__ = 'Gala & Schwarz'


class Translation(ObjectDecorator):
    """
        the class translation is used to translate the coordinates.
        **methods**:
        * :func:`__init__`: sets the coordinates.
        * :func:`create`: translates a planet.
    """
    def __init__(self, x, y, z, p):
        """
        :param x: x coordinate
        :param y: y coordinate
        :param z: z coordinate
        :param p: Planet object
        """
        self.p = p
        self.x = x
        self.y = y
        self.z = z

    def create(self):
        """
        is used to translate planets
        """
        glTranslatef(self.x, self.y, self.z)
        self.p.create()
