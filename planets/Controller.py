import pygame

from planets.LoadImages import *
from planets.Lighting import *

__author__ = 'Gala & Schwarz'


class Controller:

    def __init__(self):
        # control variables
        self.r_speed = 1
        self.light = False
        self.textures = False
        self.stop = False
        self.zoom = 0

        # camera controlling
        self.mid = True
        self.top = False
        self.bot = False
        self.cam_y = 25.
        self.cam_z = -25.

        # set up the light
        Lighting()

        # planet textures
        i = LoadImages()
        self.sun_tex = i.load("pics/sunmap.jpg")
        self.earth_tex = i.load("pics/earthmap.jpg")
        self.moon_tex = i.load("pics/moonmap.jpg")
        self.mars_tex = i.load("pics/marsmap.jpg")
        self.saturn_tex = i.load("pics/saturnmap.jpg")

        # button textures
        self.b1_tex = i.load("pics/b1.jpg")
        self.b2_tex = i.load("pics/b2.jpg")
        self.legend_tex = i.load("pics/legend.jpg")
        self.rb1_tex = i.load("pics/rb1.jpg")
        self.rb2_tex = i.load("pics/rb2.jpg")

        # speed of the different planets
        self.earth_r_speed = 0
        self.moon_r_speed = 0
        self.mars_r_speed = 0
        self.saturn_r_speed = 0
        self.saturn_ring_speed = -1*self.r_speed

        # mouse coordinates
        self.x = .0
        self.y = .0

    def key_pressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.r_speed += 1
            if event.key == pygame.K_DOWN:
                self.r_speed -= 1

            if event.key == pygame.K_w:
                self.cam_control("up")
            if event.key == pygame.K_s:
                self.cam_control("down")

            if event.key == pygame.K_p:
                self.stop = not self.stop

            if event.key == pygame.K_l:
                self.light = not self.light

            if event.key == pygame.K_t:
                self.textures = not self.textures

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if -780 <= self.x <= -550:
                    if -430 <= self.y <= -330:
                        self.light = not self.light
                    elif -310 <= self.y <= -215:
                        self.textures = not self.textures

                if -30 <= self.x <= 30:
                    if 400 <= self.y <= 430:
                        self.cam_control("down")
                    if -440 <= self.y <= -410:
                        self.cam_control("up")

                if -780 <= self.x <= -740:
                    if -155 <= self.y <= -115:
                        self.r_speed += 1
                    if -105 <= self.y <= -70:
                        self.r_speed -= 1

            if event.button == 4:
                self.r_speed += 1
            if event.button == 5:
                self.r_speed -= 1

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def cam_control(self, move):
        if move == "up":
            if self.mid:
                self.top = not self.top
                self.mid = not self.mid
                for i in range(25):
                    self.cam_y += 1
                    self.cam_z += 1
                    if self.cam_y == 25.1:
                        self.cam_y = 25
            elif self.bot:
                self.mid = not self.mid
                self.bot = not self.bot
                for i in range(25):
                    self.cam_y += 1
                    self.cam_z += 1
                    if self.cam_y == 25.1:
                        self.cam_y = 25
            elif self.top:
                pass

        elif move == "down":
            if self.mid:
                self.bot = not self.bot
                self.mid = not self.mid
                for i in range(25):
                    self.cam_y -= 1
                    self.cam_z -= 1
                    if self.cam_y == 0:
                        self.cam_y = 0.1
            elif self.top:
                self.mid = not self.mid
                self.top = not self.top
                for i in range(25):
                    self.cam_y -= 1
                    self.cam_z -= 1
                    if self.cam_y == 0:
                        self.cam_y = 0.1
            elif self.bot:
                pass

    def stopped(self):
        while self.stop:
            for event in pygame.event.get():
                self.key_pressed(event)

    def light_on_off(self):
        if not self.light:
            glDisable(GL_LIGHTING)
        else:
            glEnable(GL_LIGHTING)

    def button_textures_on(self, n):
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        if n == "b1":
            glBindTexture(GL_TEXTURE_2D, self.b1_tex)
        elif n == "b2":
            glBindTexture(GL_TEXTURE_2D, self.b2_tex)
        elif n == "legend":
            glBindTexture(GL_TEXTURE_2D, self.legend_tex)
        elif n == "rb1":
            glBindTexture(GL_TEXTURE_2D, self.rb1_tex)
        elif n == "rb2":
            glBindTexture(GL_TEXTURE_2D, self.rb2_tex)

    def textures_on_off(self, n):
        if not self.textures:
            glBindTexture(GL_TEXTURE_2D, 0)
        else:
            glEnable(GL_TEXTURE_2D)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

            if n == "sun":
                glBindTexture(GL_TEXTURE_2D, self.sun_tex)
            elif n == "earth":
                glBindTexture(GL_TEXTURE_2D, self.earth_tex)
            elif n == "moon":
                glBindTexture(GL_TEXTURE_2D, self.moon_tex)
            elif n == "mars":
                glBindTexture(GL_TEXTURE_2D, self.mars_tex)
            elif n == "saturn":
                glBindTexture(GL_TEXTURE_2D, self.saturn_tex)

    def get_mouse_pos(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.x -= 800
        self.y -= 450

    def increase(self):
        self.earth_r_speed += 0.5 * self.r_speed
        self.moon_r_speed += 3 * self.r_speed
        self.mars_r_speed += 0.3 * self.r_speed
        self.saturn_r_speed += 0.1 * self.r_speed
