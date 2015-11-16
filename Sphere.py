from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *


class Sphere(object):

    def __init__(self, r, lats, longs):
        self.r = r
        self.lats = lats
        self.longs = longs
        self.rotate = 1
        self.perspective = 50

    def draw_sphere(self):
        for i in range(self.lats + 1):
            lat0 = pi * (-0.5 + float(float(i - 1) / float(self.lats)))
            z0 = sin(lat0) * self.r
            zr0 = cos(lat0)

            lat1 = pi * (-0.5 + float(float(i) / float(self.lats)))
            z1 = sin(lat1) * self.r
            zr1 = cos(lat1)

            glBegin(GL_LINE_LOOP)

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
        glBegin(GL_LINE_LOOP)

        sphere = gluNewQuadric()
        # gluQuadricDrawStyle(sphere, GLU_FILL)
        gluSphere(sphere, self.r, self.lats, self.longs)
        # gluDeleteQuadric(sphere)

        print(glGetError())
        glEnd()

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

    def light2(self):
        zeros = (0.15, 0.15, 0.15, 0.3)
        ones = (1.0, 1.0, 1.0, 0.3)
        half = (0.5, 0.5, 0.5, 0.5)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
        glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
        glLightfv(GL_LIGHT0, GL_SPECULAR, half)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)

        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)
