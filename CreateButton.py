from Controller import *
from OpenGL.GL import *


class CreateButton:

    def __init__(self, button_name):
        self.bn = button_name
        self.c = Controller()

    def init(self):
        glPushMatrix()

        glRotatef(-45, 1., .0, .0)
        glDisable(GL_LIGHTING)

        glBegin(GL_QUADS)
        self.create()
        glEnd()

        glPopMatrix()

    def create(self):
        if self.bn == "b1":
            glColor3f(.3, .3, .3)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 13)

            glTexCoord2f(1, 1)
            glVertex2f(-40, 16)

            glTexCoord2f(0, 1)
            glVertex2f(-30, 16)

            glTexCoord2f(0, 0)
            glVertex2f(-30, 13)

        if self.bn == "b2":
            glColor3f(.3, .3, .3)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 9)

            glTexCoord2f(1, 1)
            glVertex2f(-40, 12)

            glTexCoord2f(0, 1)
            glVertex2f(-30, 12)

            glTexCoord2f(0, 0)
            glVertex2f(-30, 9)
