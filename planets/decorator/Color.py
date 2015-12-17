from OpenGL.GL import *

from planets.decorator.ObjectDecorator import *

__author__ = 'Gala & Schwarz'


class Color(ObjectDecorator):
    """
    Color is used to color thing.
    **methods**:
        * :func:`__init__`: sets the rgb on a planet.
        * :func:`create`: sets the color.
    """
    def __init__(self, r, g, b, p):
        """
        :param r: red color amount
        :param g: greed color amount
        :param b: blue color amount
        """
        self.p = p
        self.r = r
        self.g = g
        self.b = b

    def create(self):
        """
        creats the color
        """
        glColor3f(self.r, self.g, self.b)
        self.p.create()
