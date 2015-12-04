from planets.Controller import *

from planets.factory.SolarSystemFactory import *
from planets.factory.Planet import *
from planets.factory.Button import *

from planets.decorator.Translation import *
from planets.decorator.Rotation import *
from planets.decorator.Color import *
from planets.decorator.Ring import *

__author__ = 'Gala & Schwarz'


class Animate(SolarSystemFactory):

    def __init__(self):
        # Controller
        self.c = Controller()

        # Object used to create things
        self.o = Object()

        # Quadrick used for Spheres
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

            # creating light button
            glPushMatrix()
            self.c.textures_on_off("b1")
            glDisable(GL_LIGHTING)
            self.o = Rotation(45, .0, .0, 1.0,
                              Color(.3, .3, .3,
                                    Button("b1")))
            self.o.create()
            glPopMatrix()

            # creating texture button
            glPushMatrix()
            self.c.textures_on_off("b2")
            self.o = Rotation(90, 1., .0, .0,
                              Color(.3, .3, .3,
                                    Button("b2")))
            self.o.create()
            glPopMatrix()

            glPushMatrix()
            self.o = Rotation(90, 1., .0, .0,
                              Color(.7, .7, .7,
                                    Button("tb1")))
            self.o.create()
            glPopMatrix()

            glPushMatrix()
            self.o = Rotation(90, 1., .0, .0,
                              Color(.7, .7, .7,
                                    Button("tb2")))
            self.o.create()
            glPopMatrix()

            glPushMatrix()
            self.c.textures_on_off("legend")
            self.o = Rotation(90, 1., .0, .0,
                              Color(.3, .3, .3,
                                    Button("legend")))
            self.o.create()
            glPopMatrix()

            glPushMatrix()
            gluLookAt(.0, self.c.cam_y, self.c.cam_z,
                      .0, .0, .0,
                      .0, .0, 1.0)

            # creating sun
            glPushMatrix()
            self.c.textures_on_off("sun")
            glDisable(GL_LIGHTING)
            self.o = Rotation(-90, 1., .0, .0,
                              Color(1.0, 1.0, .0,
                                    Planet(self.q, 5., 30, 30)))
            self.o.create()
            glPopMatrix()

            # testing if light got turned on or off
            self.c.light_on_off()

            # creating earth
            glPushMatrix()
            self.c.textures_on_off("earth")
            glRotatef(self.c.earth_r_speed, .0, 1.0, .0)
            self.o = Translation(15.0, .0, .0,
                                 Rotation(-90, 1., .0, .0,
                                          Color(.0, 1., .0,
                                                Planet(self.q, 1.25, 30, 30))))
            self.o.create()

            self.c.textures_on_off("moon")
            glRotatef(self.c.moon_r_speed, .0, .0, 1.0)
            self.o = Translation(2., .0, .0,
                                 Color(.5, .5, .5,
                                       Planet(self.q, .25, 30, 30)))
            self.o.create()
            glPopMatrix()

            # creating mars
            glPushMatrix()
            self.c.textures_on_off("mars")
            glRotatef(self.c.mars_r_speed, .0, 1.0, .0)
            self.o = Translation(-10., .0, .0,
                                 Rotation(-90, 1., .0, .0,
                                          Color(1., .34, .04,
                                                Planet(self.q, 1.25, 30, 30))))
            self.o.create()
            glPopMatrix()

            # creating saturn
            glPushMatrix()
            self.c.textures_on_off("saturn")
            glRotatef(self.c.saturn_r_speed, .0, 1.0, .0)
            self.o = Translation(-22., .0, .0,
                                 Ring(10,
                                      Rotation(-90, 1., .0, .0,
                                               Color(.0, .0, 1.,
                                                     Planet(self.q, 1.5, 30, 30)))))
            self.o.create()
            glPopMatrix()

            glPopMatrix()

            # Redrawing everything
            pygame.display.flip()

            # Delay
            pygame.time.wait(10)
