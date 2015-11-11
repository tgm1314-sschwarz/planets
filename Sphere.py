import pygame
from pygame.locals import *
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

    def draw_sphere(self):
        for i in range(self.lats + 1):
            lat0 = pi * (-0.5 + float(float(i - 1) / float(self.lats)))
            z0 = sin(lat0)
            zr0 = cos(lat0)

            lat1 = pi * (-0.5 + float(float(i) / float(self.lats)))
            z1 = sin(lat1)
            zr1 = cos(lat1)

            #glBegin(GL_POINTS)
            #glBegin(GL_LINE_STRIP)
            glBegin(GL_QUAD_STRIP)

            for j in range(self.longs + 1):
                lng = 2 * pi * float(float(j - 1) / float(self.longs))
                x = cos(lng)
                y = sin(lng)

                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)

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




def main():
    pygame.init()
    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    #camera settings
    gluPerspective(50.0, (display[0]/display[1]), 1, 50.0)
    glTranslatef(0.0, 0.0, -10.0)

    s = Sphere(1.0, 50, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    s.rotate += 1
                if event.key == pygame.K_DOWN:
                    s.rotate -= 1
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(s.rotate, 10, 10, 10)


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        s.draw_sphere()




        s.light()



        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
