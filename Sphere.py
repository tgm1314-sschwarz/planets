import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *


class Sphere(object):

    def __init__(self, r, lats, longs, pos):
        self.r = r
        self.lats = lats
        self.longs = longs
        self.pos = pos
        self.rotate = 1
        self.perspective = 50

    def draw_sphere(self):
        for i in range(self.lats + 1):
            lat0 = pi * (-0.5 + float(float(i - 1) / float(self.lats)))
            z0 = sin(lat0) * self.r
            zr0 = cos(lat0)

            lat1 = pi * (-0.5 + float(float(i) / float(self.lats)))
            z1 = sin(lat1) *self.r
            zr1 = cos(lat1)


            glBegin(GL_LINE_STRIP)

            for j in range(self.longs + 1):
                lng = 2 * pi * float(float(j - 1) / float(self.longs))
                x = cos(lng) * self.r
                y = sin(lng) * self.r

                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)

            glEnd()

    def draw_sphere2(self):
        pass

    def light(self):
        sun1 = (0.0, 2.0, -1.0, 1.0)
        sun2 = (0.7, 0.7, 0.7, 1.0)
        intense = (0.3, 0.3, 0.3, 1.0)

        glEnable(GL_LIGHTING)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, intense)

        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, sun1)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, sun2)

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    def position(self):
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
