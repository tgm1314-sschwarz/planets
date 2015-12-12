from PIL.Image import open
from OpenGL.GL import *

__author__ = 'Gala & Schwarz'


class LoadImages:
    """
    Class that loads the images for the buttns and also for the planets

    **methods**:
        * :func:`load`: loads an image with PIL and returns the imgID of the loaded img
    """

    @staticmethod
    def load(file):
        """
        loads an image with PIL.

        :param file: name of the file you want to load
        :return: imgID of the img that got loaded
        """
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
