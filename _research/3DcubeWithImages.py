import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL.Image import open


verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

imagemap = (
    (1, 0),
    (1, 1),
    (0, 1),
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 0),
    (0, 1)
)


def cube():
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 1.0); glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, 1.0); glTexCoord2f(1.0, 1.0); glVertex3f( 1.0, 1.0, 1.0); glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, 1.0); glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0); glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, -1.0); glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, 1.0, -1.0); glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0); glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, -1.0); glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, 1.0, 1.0); glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, 1.0, 1.0); glTexCoord2f(1.0, 1.0); glVertex3f( 1.0, 1.0, -1.0); glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0); glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0); glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, 1.0); glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, 1.0); glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0); glTexCoord2f(1.0, 1.0); glVertex3f( 1.0, 1.0, -1.0); glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, 1.0, 1.0); glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, 1.0); glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0); glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, 1.0); glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, 1.0); glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, -1.0); glEnd()


def image(file):
    im = open(file)

    try:
        ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBA", 0, -1)
    except SystemError:
        ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)

    ID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, ID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

    return ID


def setup(imageID):
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    glBindTexture(GL_TEXTURE_2D, imageID)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    bg = image('../pics/earthmap.jpg')
    setup(bg)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(.0, .0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
