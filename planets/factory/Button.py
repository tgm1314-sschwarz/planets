from OpenGL.GL import *

from planets.factory.Object import *


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
            glVertex2f(-32, 16)
            glTexCoord2f(0, 0)
            glVertex2f(-32, 13)

            glEnd()

        elif self.n == "b2":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 9)
            glTexCoord2f(1, 1)
            glVertex2f(-40, 12)
            glTexCoord2f(0, 1)
            glVertex2f(-32, 12)
            glTexCoord2f(0, 0)
            glVertex2f(-32, 9)

            glEnd()

        elif self.n == "legend":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(40, -5)
            glTexCoord2f(1, 1)
            glVertex2f(40, 16)
            glTexCoord2f(0, 1)
            glVertex2f(25, 16)
            glTexCoord2f(0, 0)
            glVertex2f(25, -5)

            glEnd()

        elif self.n == "tb1":
            glBegin(GL_TRIANGLES)

            glVertex2f(0, -28)
            glVertex2f(-1.5, -26.5)
            glVertex2f(1.5, -26.5)

            glEnd()

        elif self.n == "tb2":
            glBegin(GL_TRIANGLES)

            glVertex2f(0, 16.5)
            glVertex2f(-1.5, 15)
            glVertex2f(1.5, 15)

            glEnd()
