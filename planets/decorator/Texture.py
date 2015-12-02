from OpenGL.GL import *

from planets.decorator.ObjectDecorator import *


class Texture(ObjectDecorator):

    def __init__(self, name):
        self.name = name

    def create(self):
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        if self.name == "sun":
            # glBindTexture(GL_TEXTURE_2D, self.ID[0])
            print("sun")
        elif self.name == "earth":
            glBindTexture(GL_TEXTURE_2D, self.ID[1])
        elif self.name == "moon":
            glBindTexture(GL_TEXTURE_2D, self.ID[2])
        elif self.name == "mars":
            glBindTexture(GL_TEXTURE_2D, self.ID[3])
        elif self.name == "saturn":
            glBindTexture(GL_TEXTURE_2D, self.ID[4])
        elif self.name == "b1":
            glBindTexture(GL_TEXTURE_2D, self.ID[5])
        elif self.name == "b2":
            glBindTexture(GL_TEXTURE_2D, self.ID[6])
