from OpenGL.GL import *
from OpenGL.GLU import *

from Planet import Planet
from RealPlanet import RealPlanet

from decorator.Translation import Translation
from decorator.Rotation import Rotation
from decorator.Color import Color
from decorator.HasMoon import HasMoon

__author__ = 'Gala & Schwarz'


class CreateObject:

    def __init__(self, o_name):
        self.p = Planet()
        self.o_name = o_name
        self.q = gluNewQuadric()

    def create(self):
        if self.o_name == "sun":
            glDisable(GL_LIGHTING)
            self.p = Rotation(-90, 1.0, .0, .0)
            self.p = Color(1.0, 1.0, .0)
            self.p = RealPlanet(self.q, 5, 30, 30)

        elif self.o_name == "earth":
            self.p = Translation(15.0, .0, .0)
            self.p = Rotation(-90, 1.0, .0, .0)
            self.p = Color(.0, 1.0, .0)
            self.p = RealPlanet(self.q, 1.25, 30, 30)
            """
            self.p = Translation(2.0, .0, .0)
            self.p = Color(.5, .5, .5)
            self.p = HasMoon(self.q, .25, 30, 30)
            """

        elif self.o_name == "moon":
            self.p = Translation(2.0, .0, .0)
            self.p = Color(.5, .5, .5)
            self.p = RealPlanet(self.q, .25, 30, 30)

        elif self.o_name == "mars":
            self.p = Translation(-10.0, .0, .0)
            self.p = Rotation(-90, 1.0, .0, .0)
            self.p = Color(1.0, .34, .04)
            self.p = RealPlanet(self.q, 1.25, 30, 30)

        elif self.o_name == "saturn":
            self.p = Translation(-22.0, .0, .0)
            self.p = Rotation(-90, 1.0, .0, .0)
            self.p = Color(.0, .0, 1.0)
            self.p = RealPlanet(self.q, 1.5, 30, 30)
