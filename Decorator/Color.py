from OpenGL.GL import *
from decorator.ObjectDecorator import ObjectDecorator


class Color(ObjectDecorator):

    def __init__(self, r, g, b, p):
        self.p = p
        self.r = r
        self.g = g
        self.b = b

    def create(self):
        glColor3f(self.r, self.g, self.b)
        self.p.create()
