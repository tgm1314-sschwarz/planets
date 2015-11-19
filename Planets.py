<<<<<<< HEAD
=======
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
>>>>>>> origin/master
from Sphere import *
from Images import *
from Controller import *

__author__ = 'Gala & Schwarz'


class Planets:

    def __init__(self):
        # Controller Object
        self.c = Controller()

        # sphere objects
        self.sun = Sphere(3, 30, 30, 'pics/earthmap.bmp')
        self.earth = Sphere(1.25, 30, 30, 'pics/earthmap.bmp')
        self.moon = Sphere(.25, 30, 30, 'pics/earthmap.bmp')
        self.mars = Sphere(1.25, 30, 30, 'pics/earthmap.bmp')
        self.venus = Sphere(1.5, 30, 30, 'pics/earthmap.bmp')

<<<<<<< HEAD
=======
        # speed of the different planets
        self.earthrspeed = 0
        self.moonrspeed = 0
        self.marsrspeed = 0
        self.venusrspeed = 0

>>>>>>> origin/master
        self.animation()

    def animation(self):
        while True:
            for event in pygame.event.get():
                self.c.key_pressed(event)

            # testing if the game got paused
            self.c.stopped()

            # increasing the speed
            self.c.earth_r_speed += 2 * self.c.r_speed
            self.c.moon_r_speed += 5 * self.c.r_speed
            self.c.mars_r_speed += 1 * self.c.r_speed
            self.c.venus_r_speed += 3 * self.c.r_speed

            # clearing the window
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Sun
            glPushMatrix()
            glDisable(GL_LIGHTING)          # disable light for the sun
            glColor3f(1.0, 1.0, .0)
            self.sun.draw_sphere()          # glutSolidSphere(2.0, 30, 30)
            glEnable(GL_LIGHTING)           # enable light for other planets
            glPopMatrix()

            # setting up light if L got pressed
            if self.c.light:
                glDisable(GL_LIGHTING)
            else:
                glEnable(GL_LIGHTING)

            # Earth
            glPushMatrix()
            glRotatef(self.c.earth_r_speed, .0, 1.0, .0)
            glTranslatef(15.0, .0, .0)
            glColor3f(.0, 1.0, .0)
            self.earth.draw_sphere()
            # Moon
            glRotatef(self.c.moon_r_speed, 0, 1, 0)
            glTranslatef(2.0, .0, .0)
            glColor3f(.5, .5, .5)
            self.moon.draw_sphere()
            glPopMatrix()

            # Mars
            glPushMatrix()
            glRotatef(self.c.mars_r_speed, .0, 1.0, .0)
            glTranslatef(-20.0, .0, .0)
            glColor3f(1.0, .34, .04)
            self.mars.draw_sphere()         # glutSolidSphere(1.0, 30, 30)
            glPopMatrix()

            # Venus
            glPushMatrix()
            glRotatef(self.c.venus_r_speed, .0, 1.0, .0)
            glTranslatef(-10.0, .0, .0)
            glColor3f(.0, .0, 1.0)
            self.venus.draw_sphere()
            glPopMatrix()

            # Redrawing everything
            pygame.display.flip()

            # Delay
            pygame.time.wait(10)
