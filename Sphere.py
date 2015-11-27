from OpenGL.GL import *
from OpenGL.GLU import *

from Planet import Planet
from RealPlanet import RealPlanet
from decorator.Translate import Translate
from decorator.Rotate import Rotate
from decorator.Color import Color
from decorator.HasMoon import HasMoon

__author__ = 'Gala & Schwarz'


class Sphere:

    def __init__(self, planet_name):
        self.p = Planet()
        self.p_name = planet_name
        self.q = gluNewQuadric()

    def create_sphere(self):
        if self.p_name == "sun":
            glDisable(GL_LIGHTING)
            self.p = Rotate(-90, 1.0, .0, .0)
            self.p = Color(1.0, 1.0, .0)
            self.p = RealPlanet(self.q, 5, 30, 30)

        elif self.p_name == "earth":
            self.p = Translate(15.0, .0, .0)
            self.p = Rotate(-90, 1.0, .0, .0)
            self.p = Color(.0, 1.0, .0)
            self.p = RealPlanet(self.q, 1.25, 30, 30)

        elif self.p_name == "moon":
            self.p = Translate(2.0, .0, .0)
            self.p = Color(.5, .5, .5)
            self.p = RealPlanet(self.q, .25, 30, 30)

        elif self.p_name == "mars":
            self.p = Translate(-10.0, .0, .0)
            self.p = Rotate(-90, 1.0, .0, .0)
            self.p = Color(1.0, .34, .04)
            self.p = RealPlanet(self.q, 1.25, 30, 30)

        elif self.p_name == "saturn":
            self.p = Translate(-22.0, .0, .0)
            self.p = Rotate(-90, 1.0, .0, .0)
            self.p = Color(.0, .0, 1.0)
            self.p = RealPlanet(self.q, 1.5, 30, 30)

    """
    def __init__(self, r, lats, longs, q):
        self.r = r
        self.lats = lats
        self.longs = longs
        self.q = q


    def draw_sphere(self):
        texY1 = 0
        for i in range(self.lats + 1):
            texY0 = texY1
            lat0 = pi * (-0.5 + float(float(i - 1) / float(self.lats)))
            z0 = sin(lat0) * self.r
            zr0 = cos(lat0)

            lat1 = pi * (-0.5 + float(float(i) / float(self.lats)))
            z1 = sin(lat1) * self.r
            zr1 = cos(lat1)

            texY1 = float(i)/float(self.lats)

            glBegin(GL_QUAD_STRIP)

            for j in range(self.longs + 1):
                texX = float(j)/float(self.longs)
                lng = 2 * pi * float(float(j - 1) / float(self.longs))
                x = cos(lng) * self.r
                y = sin(lng) * self.r

                glTexCoord2f(texX, texY1)
                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)

                glTexCoord2f(texX, texY0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)

            glEnd()

    def draw_sphere2(self):
        gluQuadricTexture(self.q, 1)
        gluSphere(self.q, self.r, self.lats, self.longs)
    """
