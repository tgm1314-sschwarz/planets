from CreateObject import *
from CreateButton import *
from Controller import *

__author__ = 'Gala & Schwarz'


class Animate:

    def __init__(self):
        # Controller Object
        self.c = Controller()

        # planets
        self.sun = CreateObject("sun")
        self.earth = CreateObject("earth")
        self.moon = CreateObject("moon")
        self.mars = CreateObject("mars")
        self.saturn = CreateObject("saturn")

        # buttons
        """
        self.b1 = CreateObject("b1")
        self.b2 = CreateObject("b2")
        """
        self.b1 = CreateButton("b1")
        self.b2 = CreateButton("b2")

        # starting to animate
        self.animation()

    def animation(self):
        while True:
            # get the OpenGL coordinates of the mouse position
            self.c.get_mouse_pos()

            # testing if a key got pressed
            for event in pygame.event.get():
                self.c.key_pressed(event)

            # testing if the game got paused
            self.c.stopped()

            # increasing the speed
            self.c.increase()

            # clearing the window and starting to draw
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # drawing the buttons
            glPushMatrix()
            self.c.textures_on_off("b1")
            self.b1.init()
            self.c.textures_on_off("b2")
            self.b2.init()
            glPopMatrix()
            """
            glPushMatrix()
            self.c.textures_on_off("b1")
            self.b1.create()
            self.c.textures_on_off("b2")
            self.b2.create()
            glPopMatrix()
            """

            glPushMatrix()
            self.c.textures_on_off("sun")
            self.sun.create()
            glPopMatrix()

            # testing if light got turned on or off
            self.c.light_on_off()

            glPushMatrix()
            self.c.textures_on_off("earth")
            glRotatef(self.c.earth_r_speed, .0, 1.0, .0)
            self.earth.create()

            self.c.textures_on_off("moon")
            glRotatef(self.c.moon_r_speed, .0, .0, 1.0)
            self.moon.create()
            glPopMatrix()

            glPushMatrix()
            self.c.textures_on_off("mars")
            glRotatef(self.c.mars_r_speed, .0, 1.0, .0)
            self.mars.create()
            glPopMatrix()

            glPushMatrix()
            self.c.textures_on_off("saturn")
            glRotatef(self.c.saturn_r_speed, .0, 1.0, .0)
            self.saturn.create()
            glPopMatrix()

            """
            # Ring
            glRotatef(45, .0, 1.0, .0)
            for i in range(10):
                glutWireTorus(0.1, 2+(i*0.1), 30, 30)
            """
            # Redrawing everything
            pygame.display.flip()

            # Delay
            pygame.time.wait(10)
