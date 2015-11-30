from OpenGL.GL import *
from OpenGL.GLU import *

from Object import Object
from Planet import Planet
from Button import Button
from decorator.Translation import Translation
from decorator.Rotation import Rotation
from decorator.Color import Color

__author__ = 'Gala & Schwarz'


class CreateObject:

    def __init__(self, o_name):
        self.o = Object()
        self.o_name = o_name
        self.q = gluNewQuadric()

    def create(self):
        if self.o_name == "sun":
            glDisable(GL_LIGHTING)
            self.o = Rotation(-90, 1., .0, .0,
                              Color(1.0, 1.0, .0,
                                    Planet(self.q, 5., 30, 30)))
            self.o.create()

        elif self.o_name == "earth":
            self.o = Translation(15.0, .0, .0,
                                 Rotation(-90, 1., .0, .0,
                                          Color(.0, 1., .0,
                                                Planet(self.q, 1.25, 30, 30))))
            self.o.create()

        elif self.o_name == "moon":
            self.o = Translation(2., .0, .0,
                                 Color(.5, .5, .5,
                                       Planet(self.q, .25, 30, 30)))
            self.o.create()

        elif self.o_name == "mars":
            self.o = Translation(-10., .0, .0,
                                 Rotation(-90, 1., .0, .0,
                                          Color(1., .34, .04,
                                                Planet(self.q, 1.25, 30, 30))))
            self.o.create()

        elif self.o_name == "saturn":
            self.o = Translation(-22., .0, .0,
                                 Rotation(-90, 1., .0, .0,
                                          Color(.0, .0, 1.,
                                                Planet(self.q, 1.5, 30, 30))))
            self.o.create()

        elif self.o_name == "b1":
            glDisable(GL_LIGHTING)
            self.o = Rotation(-45, 1., .0, .0,
                              Color(.3, .3, .3,
                                    Button("b1")))
            self.o.create()
