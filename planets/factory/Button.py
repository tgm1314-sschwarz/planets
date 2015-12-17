from OpenGL.GL import *

from planets.factory.Object import *

__author__ = 'Gala & Schwarz'


class Button(Object):
    """
    Class button creates rectangles with textures that serve as buttons.

    **methods**:
        * :func:`__init__`: sets the button name.
        * :func:`create`: defines the texture and the clickable area.
    """

    def __init__(self, button_name):
        """
        sets the button name
        :param button_name: name of the created button
        """
        self.n = button_name

    def create(self):
        """
        defines the texture and the clickable area.
        """
        if self.n == "b1":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 11)
            glTexCoord2f(1, 1)
            glVertex2f(-40, 16)
            glTexCoord2f(0, 1)
            glVertex2f(-28, 16)
            glTexCoord2f(0, 0)
            glVertex2f(-28, 11)

            glEnd()

        elif self.n == "b2":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 5)
            glTexCoord2f(1, 1)
            glVertex2f(-40, 10)
            glTexCoord2f(0, 1)
            glVertex2f(-28, 10)
            glTexCoord2f(0, 0)
            glVertex2f(-28, 5)

            glEnd()

        elif self.n == "rb1":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(-40, 0)
            glTexCoord2f(1, 1)
            glVertex2f(-40, 2)
            glTexCoord2f(0, 1)
            glVertex2f(-38, 2)
            glTexCoord2f(0, 0)
            glVertex2f(-38, 0)

            glEnd()

        elif self.n == "rb2":
            glBegin(GL_QUADS)

            glTexCoord2f(1, 0)
            glVertex2f(-40, -2.5)
            glTexCoord2f(1, 1)
            glVertex2f(-40, -0.5)
            glTexCoord2f(0, 1)
            glVertex2f(-38, -0.5)
            glTexCoord2f(0, 0)
            glVertex2f(-38, -2.5)

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
