from OpenGL.GLU import *
from pygame.locals import *
from Lighting import *
from Planets import *
from Controller import *

__author__ = 'Gala & Schwarz'


def main():

    # window Position
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 100)

    pygame.init()

    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glShadeModel(GL_SMOOTH)
    glClearColor(.0, .0, .0, .0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)

    gluPerspective(75, (display[0]/display[1]), 1, 50.0)
    glTranslatef(.0, 6.0, -30)
    glRotatef(45.0, 1.0, .0, .0)

    glMatrixMode(GL_MODELVIEW)

    glutInit()

    # set up the light
    Lighting()

    # draw the planets
    Planets()


if __name__ == '__main__':
    main()
