from PIL.Image import open
from OpenGL.GL import *

__author__ = 'Gala & Schwarz'


class LoadImages:

    @staticmethod
    def load(file):

        img = open(file)

        try:
            ix, iy, image = img.size[0], img.size[1], img.tobytes("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = img.size[0], img.size[1], img.tobytes("raw", "RGBX", 0, -1)

        imgID = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, imgID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return imgID

    """
    @staticmethod
    def place_image(imgID):
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        glBindTexture(GL_TEXTURE_2D, imgID)
    """
