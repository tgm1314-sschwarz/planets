from decorator.ObjectDecorator import ObjectDecorator
from OpenGL.GL import *
from OpenGL.GLUT import *


class Ring(ObjectDecorator):

    def __init__(self, r, p):
        self.p = p
        self.r = r

    def create(self):
        glPushMatrix()

        glColor3f(.8, .8, .8)
        glRotatef(-90, 1., .0, .0)

        for i in range(self.r):
            glutWireTorus(0.1, 2+(i*0.1), 30, 30)

        glPopMatrix()

        self.p.create()
