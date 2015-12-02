from OpenGL.GL import *

from planets.decorator.ObjectDecorator import *


class Rotation(ObjectDecorator):

    def __init__(self, deg, x, y, z, p):
        self.p = p
        self.deg = deg
        self.x = x
        self.y = y
        self.z = z

    def create(self):
        glRotatef(self.deg, self.x, self.y, self.z)
        self.p.create()
