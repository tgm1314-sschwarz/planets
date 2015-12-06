from planets.Controller import *

from planets.factory.SolarSystemFactory import *
from planets.factory.Planet import *
from planets.factory.Button import *

from planets.decorator.Translation import *
from planets.decorator.Rotation import *
from planets.decorator.Color import *
from planets.decorator.Orbit import *
from planets.decorator.Moon import *
from planets.decorator.Ring import *

__author__ = 'Gala & Schwarz'


class SolarSystem(SolarSystemFactory):

    def __init__(self):
        # Controller
        self.c = Controller()

        # Object used to create things
        self.o = Object()

        # gluNewQuadric used for Spheres
        self.q = gluNewQuadric()

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

            # open button view
            glPushMatrix()

            # creating the camera for the buttons, so they don't change
            # if the planet camera is changed
            gluLookAt(.0, 0, -30.0,
                      .0, .0, .0,
                      .0, 1.0, .0)
            glTranslatef(.0, 6.0, .0)
            glRotatef(180, .0, 1.0, .0)
            glDisable(GL_LIGHTING)

            # creating light button
            self.c.button_textures_on("b1")
            self.o = Button("b1")
            self.o.create()

            # creating texture button
            self.c.button_textures_on("b2")
            self.o = Button("b2")
            self.o.create()

            # creating in and decrease rotation speed button
            self.c.button_textures_on("rb1")
            self.o = Button("rb1")
            self.o.create()
            self.c.button_textures_on("rb2")
            self.o = Button("rb2")
            self.o.create()

            # creating triangle up and down button
            self.o = Color(.7, .7, .7,
                           Button("tb1"))
            self.o.create()
            self.o = Color(.7, .7, .7,
                           Button("tb2"))
            self.o.create()

            # creating legend
            self.c.button_textures_on("legend")
            self.o = Color(.0, .0, .0,
                           Button("legend"))
            self.o.create()

            # close button view
            glPopMatrix()

            # open planet view
            glPushMatrix()

            # camera for planets that can be controlled
            """
            # z-upv:
            # y=50., z=0     ...90 Grad
            # y=25., z=-25   ...45 Grad
            # y=.1, z=-50    ...0 Grad
            """
            gluLookAt(.0, self.c.cam_y, self.c.cam_z,
                      .0, .0, .0,
                      .0, .0, 1.0)

            # creating sun
            glPushMatrix()
            self.c.textures_on_off("sun")
            glDisable(GL_LIGHTING)
            self.o = Rotation(-90, 1., .0, .0,
                              Color(1.0, 1.0, .0,
                                    Planet(5.0)))
            self.o.create()
            glPopMatrix()

            # testing if light got turned on or off
            self.c.light_on_off()

            # creating earth
            glPushMatrix()
            self.c.textures_on_off("earth")
            glRotatef(self.c.earth_r_speed, .0, 1.0, .0)
            self.o = Orbit(15.0,
                           Translation(15.0, .0, .0,
                                       Rotation(-90, 1., .0, .0,
                                                Color(.0, 1., .0,
                                                      Planet(1.25)))))
            self.o.create()

            self.c.textures_on_off("moon")
            glRotatef(self.c.moon_r_speed, .0, .0, 1.0)
            self.o = Rotation(90, 1., .0, .0,
                              Orbit(2.0,
                                    Translation(2.0, .0, .0,
                                                Color(.5, .5, .5,
                                                      Planet(.25)))))
            self.o.create()
            glPopMatrix()

            # creating mars
            glPushMatrix()
            self.c.textures_on_off("mars")
            glRotatef(self.c.mars_r_speed, .0, 1.0, .0)
            self.o = Orbit(10.0,
                           Translation(-10., .0, .0,
                                       Rotation(-90, 1., .0, .0,
                                                Color(1., .34, .04,
                                                      Planet(1.25)))))
            self.o.create()
            glPopMatrix()

            # creating saturn
            glPushMatrix()
            self.c.textures_on_off("saturn")
            glRotatef(self.c.saturn_r_speed, .0, 1.0, .0)
            self.o = Orbit(22.0,
                           Translation(-22.0, .0, .0,
                                       Ring(10,
                                            Rotation(-90, 1., .0, .0,
                                                     Color(.0, .0, 1.,
                                                           Planet(1.5))))))
            self.o.create()
            glPopMatrix()

            # close planet view
            glPopMatrix()

            # Redrawing everything
            pygame.display.flip()

            # Delay
            pygame.time.wait(10)
