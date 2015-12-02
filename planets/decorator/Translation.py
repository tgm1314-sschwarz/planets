from OpenGL.GL import *

from planets.decorator.ObjectDecorator import *


class Translation(ObjectDecorator):

    def __init__(self, x, y, z, p):
        self.p = p
        self.x = x
        self.y = y
        self.z = z

    def create(self):
        glTranslatef(self.x, self.y, self.z)
        self.p.create()
