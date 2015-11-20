import pygame

__author__ = 'Gala & Schwarz'


class Controller:

    def __init__(self):
        # control variables
        self.r_speed = 1
        self.light = True
        self.textures = False
        self.stop = False
        self.zoom = 0

        # speed of the different planets
        self.earth_r_speed = 0
        self.moon_r_speed = 0
        self.mars_r_speed = 0
        self.saturn_r_speed = 0
        self.saturn_ring_speed = -1*self.r_speed

    def key_pressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.r_speed += 1
            if event.key == pygame.K_DOWN:
                self.r_speed -= 1

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

    def increase(self):
        self.earth_r_speed += 1 * self.r_speed
        self.moon_r_speed += 3 * self.r_speed
        self.mars_r_speed += 0.5 * self.r_speed
        self.saturn_r_speed += 0.2 * self.r_speed