from Sphere import *
from Images import *
from Controller import *

__author__ = 'Gala & Schwarz'


class Planets:

    def __init__(self):
        # Controller Object
        self.c = Controller()
        self.i = Images()

        # quadrick
        q = gluNewQuadric()

        # spheres
        self.sun = Sphere(5, 30, 30, q)
        self.earth = Sphere(1.25, 30, 30, q)
        self.moon = Sphere(.25, 30, 30, q)
        self.mars = Sphere(1.25, 30, 30, q)
        self.saturn = Sphere(1.5, 30, 30, q)

        # textures
        self.earth_tex = self.i.image("pics/earthmap.jpg")
        self.sun_tex = self.i.image("pics/sunmap.jpg")
        self.moon_tex = self.i.image("pics/moonmap.jpg")
        self.mars_tex = self.i.image("pics/marsmap.jpg")
        self.saturn_tex = self.i.image("pics/saturnmap.jpg")
        # self.saturn_ring_tex = self.i.image("pics/saturnringmap.jpg")

        # starting to animate
        self.animation()

    def animation(self):
        while True:
            # testing if a key got pressed
            for event in pygame.event.get():
                self.c.key_pressed(event)
            # testing if the game got paused
            self.c.stopped()
            # increasing the speed
            self.c.increase()

            # clearing the window and starting to draw
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Sun
            if self.c.textures: self.i.place_texture(self.sun_tex)
            glPushMatrix()
            glDisable(GL_LIGHTING)          # disable light for the sun
            glColor3f(1.0, 1.0, .0)
            self.sun.draw_sphere2()          # glutSolidSphere(2.0, 30, 30)
            glEnable(GL_LIGHTING)           # enable light for other planets
            glPopMatrix()

            # disable light if "l" got pressed
            if self.c.light:
                glDisable(GL_LIGHTING)
            else:
                glEnable(GL_LIGHTING)

            # Earth + Moon
            if self.c.textures: self.i.place_texture(self.earth_tex)
            glPushMatrix()
            # Earth
            glRotatef(-90, 1.0, .0, .0)
            glRotatef(self.c.earth_r_speed, .0, .0, 1.0)
            glTranslatef(15.0, .0, .0)
            glColor3f(.0, 1.0, .0)
            self.earth.draw_sphere2()
            # Moon
            if self.c.textures: self.i.place_texture(self.moon_tex)
            glRotatef(self.c.moon_r_speed, .0, .0, 1.0)
            glTranslatef(2.0, .0, .0)
            glColor3f(.5, .5, .5)
            self.moon.draw_sphere2()
            glPopMatrix()

            # Mars
            if self.c.textures: self.i.place_texture(self.mars_tex)
            glPushMatrix()
            glRotatef(-90, 1.0, .0, .0)
            glRotatef(self.c.mars_r_speed, .0, .0, 1.0)
            glTranslatef(-10.0, .0, .0)
            glColor3f(1.0, .34, .04)
            self.mars.draw_sphere2()
            glPopMatrix()

            # Saturn + Ring
            if self.c.textures: self.i.place_texture(self.saturn_tex)
            glPushMatrix()
            # Saturn
            glRotatef(-90, 1.0, .0, .0)
            glRotatef(self.c.saturn_r_speed, .0, .0, 1.0)
            glTranslatef(-22.0, .0, .0)
            glColor3f(.0, .0, 1.0)
            self.saturn.draw_sphere()
            """
            # Ring
            glRotatef(45, .0, 1.0, .0)
            for i in range(10):
                glutWireTorus(0.1, 2+(i*0.1), 30, 30)
            """
            glPopMatrix()

            if not self.c.textures:
                glDisable(GL_TEXTURE_2D)

            # Redrawing everything
            pygame.display.flip()

            # Delay
            pygame.time.wait(10)
