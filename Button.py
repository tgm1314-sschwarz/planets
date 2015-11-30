from Object import Object
from OpenGL.GL import *


class Button(Object):

    def __init__(self, button_name):
        self.n = button_name

    def create(self):
        if self.n == "b1":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 13)
            glTexCoord2f(1, 1)
            glVertex2f(-40, 16)
            glTexCoord2f(0, 1)
            glVertex2f(-30, 16)
            glTexCoord2f(0, 0)
            glVertex2f(-30, 13)

            glEnd()

        elif self.n == "b2":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 9)
            glTexCoord2f(1, 1)
            glVertex2f(-40, 12)
            glTexCoord2f(0, 1)
            glVertex2f(-30, 12)
            glTexCoord2f(0, 0)
            glVertex2f(-30, 9)

            glEnd()