import pygame
from OpenGL.GL import *
from LoadImage import Image

__author__ = 'Gala & Schwarz'


class Controller:

    def __init__(self):
        # control variables
        self.r_speed = 1
        self.light = False
        self.textures = False
        self.stop = False
        self.zoom = 0
        self.swagmode = False

        self.i = Image()

        self.sun_texture = self.i.load("pics/sunmap.jpg")
        self.earth_texture = self.i.load("pics/earthmap.jpg")
        self.mars_texture = self.i.load("pics/marsmap.jpg")
        self.saturn_texture = self.i.load("pics/saturnmap.jpg")

        # speed of the different planets
        self.earth_r_speed = 0
        self.moon_r_speed = 0
        self.mars_r_speed = 0
        self.saturn_r_speed = 0
        self.saturn_ring_speed = -1*self.r_speed

    def key_pressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.r_speed += 1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.r_speed -= 1

            if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                self.stop = not self.stop

            if event.key == pygame.K_l:
                self.light = not self.light

            if event.key == pygame.K_t:
                self.textures = not self.textures

            if event.key == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                self.swagmode = not self.swagmode

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.light = not self.light

            if event.button == 3:
                self.textures = not self.textures

            if event.button == 4:
                self.r_speed += 1
            if event.button == 5:
                self.r_speed -= 1

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def stopped(self):
        while self.stop:
            for event in pygame.event.get():
                self.key_pressed(event)

    def light_on_off(self):
        if not self.light:
            glDisable(GL_LIGHTING)
        else:
            glEnable(GL_LIGHTING)

    def textures_on_off(self, name):
        if not self.textures:
            glDisable(GL_TEXTURE_2D)
        else:
            glEnable(GL_TEXTURE_2D)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

            if name == "sun":
                glBindTexture(GL_TEXTURE_2D, self.sun_texture)
            elif name == "earth":
                glBindTexture(GL_TEXTURE_2D, self.earth_texture)
            elif name == "mars":
                glBindTexture(GL_TEXTURE_2D, self.mars_texture)
            elif name == "saturn":
                glBindTexture(GL_TEXTURE_2D, self.saturn_texture)

    def increase(self):
        self.earth_r_speed += 0.5 * self.r_speed
        self.moon_r_speed += 3 * self.r_speed
        self.mars_r_speed += 0.3 * self.r_speed
        self.saturn_r_speed += 0.1 * self.r_speed
