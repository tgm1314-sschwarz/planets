from Sphere import *
from Controller import *

__author__ = 'Gala & Schwarz'


class Animate:

    def __init__(self):
        # Controller Object
        self.c = Controller()

        # spheres
        self.sun = Sphere("sun")
        self.earth = Sphere("earth")
        self.mars = Sphere("mars")
        self.saturn = Sphere("saturn")

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

            self.c.textures_on_off("sun")
            glPushMatrix()
            self.sun.create_sphere()
            glPopMatrix()

            # testing if light got turned on or off
            self.c.light_on_off()

            self.c.textures_on_off("earth")
            glPushMatrix()
            glRotatef(self.c.earth_r_speed, .0, 1.0, .0)
            self.earth.create_sphere()
            glPopMatrix()

            self.c.textures_on_off("mars")
            glPushMatrix()
            glRotatef(self.c.mars_r_speed, .0, 1.0, .0)
            self.mars.create_sphere()
            glPopMatrix()

            self.c.textures_on_off("saturn")
            glPushMatrix()
            glRotatef(self.c.saturn_r_speed, .0, 1.0, .0)
            self.saturn.create_sphere()
            glPopMatrix()

            """
            # Sun
            if self.c.textures: self.i.place_texture(self.sun_tex)
            glPushMatrix()
            glDisable(GL_LIGHTING)          # disable light for the sun
            glRotatef(-90, 1.0, .0, .0)
            glColor3f(1.0, 1.0, .0)
            # glutSolidSphere(5.0, 30, 30)
            self.sun.draw_sphere2()
            glEnable(GL_LIGHTING)           # enable light for other planets
            glPopMatrix()

            # disable light if "l" got pressed
            if not self.c.light:
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
            self.saturn.draw_sphere2()

            # Ring

            glRotatef(45, .0, 1.0, .0)
            for i in range(10):
                glutWireTorus(0.1, 2+(i*0.1), 30, 30)

            glPopMatrix()

            if not self.c.textures:
                glDisable(GL_TEXTURE_2D)
            """
            # Redrawing everything
            pygame.display.flip()

            # Delay
            pygame.time.wait(10)
