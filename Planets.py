import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from Sphere import *

__author__ = 'Gala & Schwarz'


class Planets:

    def __init__(self):
        # control variables
        self.rspeed = 1
        self.earthrspeed = 0
        self.moonrspeed = 0
        self.marsrspeed = 0
        self.light = True
        self.textures = False
        self.stop = False

        # sphere objects
        self.sun = Sphere(3, 30, 30)
        self.earth = Sphere(1.25, 30, 30)
        self.moon = Sphere(.25, 30, 30)
        self.mars = Sphere(1.25, 30, 30)

        self.animation()

    def stopped(self):
        while self.stop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.stop = not self.stop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def animation(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.rspeed += 1
                    if event.key == pygame.K_DOWN:
                        self.rspeed -= 1
                    if event.key == pygame.K_p:
                        self.stop = not self.stop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.stopped()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.moonrspeed += 5 * self.rspeed
            self.marsrspeed += 1 * self.rspeed
            self.earthrspeed += 2 * self.rspeed
            #glRotatef(self.rspeed, .0, 1.0, .0)

            # Sun
            glColor3f(1.0, 1.0, 0.0)
            self.sun.draw_sphere()          # glutSolidSphere(2.0, 30, 30)

            # Earth
            glPushMatrix()
            glRotatef(self.earthrspeed, .0, 1.0, .0)
            glTranslatef(15.0, .0, .0)
            glColor3f(.0, 1.0, .0)
            self.earth.draw_sphere()        # glutSolidSphere(1.0, 30, 30)
            # Moon
            glRotatef(self.moonrspeed, 0, 1, 0)
            glTranslatef(2.0, .0, .0)
            glColor3f(.5, .5, .5)
            self.moon.draw_sphere()
            glPopMatrix()

            # Mars
            glPushMatrix()
            glRotatef(self.marsrspeed, .0, 1.0, .0)
            glTranslatef(-22.0, .0, .0)
            glColor3f(1.0, 0.34, 0.04)
            self.mars.draw_sphere()         # glutSolidSphere(1.0, 30, 30)
            glPopMatrix()

            # Redrawing everything
            pygame.display.flip()
            # Delay
            pygame.time.wait(10)
